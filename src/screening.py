from pathlib import Path

from src.parser import extract_resume_text

from src.skills import (
    extract_skills,
    calculate_skill_match,
    get_matched_skills,
    get_missing_skills
)

from src.similarity import similarity_percentage

from src.profile import (
    extract_years_of_experience,
    extract_education_level,
    experience_match,
    education_match
)

from src.scoring import (
    create_screening_result
)


# ============================================================
# SCREEN ONE RESUME
# ============================================================

def screen_resume(
    resume_path,
    job_description,
    candidate_name=None
):
    """
    Screen one candidate against a job description.

    Parameters:
        resume_path:
            Path to candidate resume.

        job_description:
            Complete job description.

        candidate_name:
            Candidate name. If not provided,
            filename will be used.

    Returns:
        Dictionary containing complete screening result.
    """

    # --------------------------------------------------------
    # Candidate name
    # --------------------------------------------------------

    if not candidate_name:

        candidate_name = Path(
            resume_path
        ).stem


    # --------------------------------------------------------
    # Extract resume text
    # --------------------------------------------------------

    resume_text = extract_resume_text(
        resume_path
    )


    if not resume_text:

        raise ValueError(
            f"Could not extract text from: "
            f"{resume_path}"
        )


    # --------------------------------------------------------
    # Extract skills
    # --------------------------------------------------------

    required_skills = extract_skills(
        job_description
    )

    candidate_skills = extract_skills(
        resume_text
    )


    # --------------------------------------------------------
    # Skill matching
    # --------------------------------------------------------

    skill_score = calculate_skill_match(
        required_skills,
        candidate_skills
    )

    matched_skills = get_matched_skills(
        required_skills,
        candidate_skills
    )

    missing_skills = get_missing_skills(
        required_skills,
        candidate_skills
    )


    # --------------------------------------------------------
    # Semantic similarity
    # --------------------------------------------------------

    semantic_score = similarity_percentage(
        job_description,
        resume_text
    )


    # --------------------------------------------------------
    # Experience
    # --------------------------------------------------------

    required_experience = (
        extract_years_of_experience(
            job_description
        )
    )

    candidate_experience = (
        extract_years_of_experience(
            resume_text
        )
    )

    experience_score = experience_match(
        required_experience,
        candidate_experience
    )


    # --------------------------------------------------------
    # Education
    # --------------------------------------------------------

    required_education = (
        extract_education_level(
            job_description
        )
    )

    candidate_education = (
        extract_education_level(
            resume_text
        )
    )

    education_score = education_match(
        required_education,
        candidate_education
    )


    # --------------------------------------------------------
    # Final scoring
    # --------------------------------------------------------

    result = create_screening_result(
        candidate_name=candidate_name,

        skill_score=skill_score,

        semantic_score=semantic_score,

        experience_score=experience_score,

        education_score=education_score
    )


    # --------------------------------------------------------
    # Add additional information
    # --------------------------------------------------------

    result["required_skills"] = (
        required_skills
    )

    result["candidate_skills"] = (
        candidate_skills
    )

    result["matched_skills"] = (
        matched_skills
    )

    result["missing_skills"] = (
        missing_skills
    )

    result["required_experience"] = (
        required_experience
    )

    result["candidate_experience"] = (
        candidate_experience
    )

    result["required_education"] = (
        required_education
    )

    result["candidate_education"] = (
        candidate_education
    )

    return result


# ============================================================
# SCREEN MULTIPLE RESUMES
# ============================================================

def screen_multiple_resumes(
    resume_paths,
    job_description
):
    """
    Screen multiple resumes against
    the same job description.

    Returns candidates ranked from
    highest score to lowest score.
    """

    results = []


    for resume_path in resume_paths:

        try:

            result = screen_resume(
                resume_path=resume_path,
                job_description=job_description
            )

            results.append(result)

        except Exception as error:

            print(
                f"Error screening "
                f"{resume_path}: {error}"
            )


    # --------------------------------------------------------
    # Rank candidates
    # --------------------------------------------------------

    results.sort(
        key=lambda result: result["final_score"],
        reverse=True
    )


    # --------------------------------------------------------
    # Add ranking position
    # --------------------------------------------------------

    for position, result in enumerate(
        results,
        start=1
    ):

        result["rank"] = position


    return results