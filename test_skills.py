from src.parser import extract_resume_text
from src.skills import (
    extract_skills,
    calculate_skill_match,
    get_matched_skills,
    get_missing_skills
)


# ============================================================
# TEST RESUME
# ============================================================

file_path = "data/resumes/test_resume.txt"

resume_text = extract_resume_text(file_path)

candidate_skills = extract_skills(resume_text)


print("\n" + "=" * 70)
print("CANDIDATE RESUME SKILLS")
print("=" * 70)

for skill in candidate_skills:
    print("✓", skill)


# ============================================================
# TEST DIFFERENT JOB DESCRIPTIONS
# ============================================================

job_descriptions = {

    "Data Analyst": """
        We are looking for a Data Analyst with experience
        in Python, SQL, Pandas, Power BI, Excel and Machine Learning.
    """,

    "Python Developer": """
        We are looking for a Python Developer with experience
        in Python, Django, Flask, REST API, MySQL and Git.
    """,

    "AI/ML Engineer": """
        We are looking for an AI/ML Engineer with experience
        in Python, Machine Learning, Deep Learning,
        TensorFlow, PyTorch and NLP.
    """,

    "HR Executive": """
        We are looking for an HR Executive with experience
        in Recruitment, Talent Acquisition, Communication,
        Interviewing and HRMS.
    """
}


# ============================================================
# TEST EACH JOB
# ============================================================

for job_role, job_description in job_descriptions.items():

    print("\n" + "=" * 70)
    print(f"JOB ROLE: {job_role}")
    print("=" * 70)

    required_skills = extract_skills(
        job_description
    )

    print("\nRequired Skills:")

    for skill in required_skills:
        print("•", skill)

    matched = get_matched_skills(
        required_skills,
        candidate_skills
    )

    missing = get_missing_skills(
        required_skills,
        candidate_skills
    )

    score = calculate_skill_match(
        required_skills,
        candidate_skills
    )

    print("\nMatched Skills:")

    for skill in matched:
        print("✓", skill)

    print("\nMissing Skills:")

    for skill in missing:
        print("✗", skill)

    print(
        f"\nSkill Match Score: {score}%"
    )