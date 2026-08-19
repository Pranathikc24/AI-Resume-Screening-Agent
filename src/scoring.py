# ============================================================
# RESUME SCREENING SCORING ENGINE
# ============================================================


def calculate_final_score(
    skill_score,
    semantic_score,
    experience_score,
    education_score
):
    """
    Calculate the final candidate screening score.

    Weight distribution:

    Skill Match          = 40%
    Semantic Similarity  = 40%
    Experience Match     = 10%
    Education Match      = 10%

    Returns:
        Final score between 0 and 100.
    """

    final_score = (
        (skill_score * 0.40)
        + (semantic_score * 0.40)
        + (experience_score * 0.10)
        + (education_score * 0.10)
    )

    return round(final_score, 2)


# ============================================================
# CANDIDATE RECOMMENDATION
# ============================================================

def get_recommendation(score):
    """
    Convert the final numerical score
    into a recruitment recommendation.
    """

    if score >= 80:
        return "Strong Match"

    elif score >= 65:
        return "Good Match"

    elif score >= 50:
        return "Potential Match"

    else:
        return "Low Match"


# ============================================================
# SCREENING RESULT
# ============================================================

def create_screening_result(
    candidate_name,
    skill_score,
    semantic_score,
    experience_score,
    education_score
):
    """
    Create a complete screening result
    for one candidate.
    """

    final_score = calculate_final_score(
        skill_score,
        semantic_score,
        experience_score,
        education_score
    )

    recommendation = get_recommendation(
        final_score
    )

    return {
        "candidate_name": candidate_name,

        "skill_score": round(
            skill_score,
            2
        ),

        "semantic_score": round(
            semantic_score,
            2
        ),

        "experience_score": round(
            experience_score,
            2
        ),

        "education_score": round(
            education_score,
            2
        ),

        "final_score": final_score,

        "recommendation": recommendation
    }


# ============================================================
# RANK CANDIDATES
# ============================================================

def rank_candidates(results):
    """
    Sort candidates from highest score
    to lowest score.
    """

    return sorted(
        results,
        key=lambda candidate: candidate["final_score"],
        reverse=True
    )