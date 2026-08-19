import re


# ============================================================
# EXPERIENCE EXTRACTION
# ============================================================

def extract_years_of_experience(text):
    """
    Extract the highest number of years of experience
    mentioned in a resume or job description.
    """

    if not text:
        return 0.0

    patterns = [
        r"(\d+(?:\.\d+)?)\s*\+?\s*years?\s*(?:of)?\s*experience",
        r"(\d+(?:\.\d+)?)\s*\+?\s*years?",
        r"experience\s*(?:of)?\s*(\d+(?:\.\d+)?)\s*\+?\s*years?"
    ]

    numbers = []

    for pattern in patterns:

        matches = re.findall(
            pattern,
            text.lower()
        )

        for match in matches:

            try:
                numbers.append(float(match))
            except ValueError:
                pass

    if not numbers:
        return 0.0

    return max(numbers)


# ============================================================
# EDUCATION EXTRACTION
# ============================================================

EDUCATION_LEVELS = {
    "phd": 5,
    "doctorate": 5,

    "master": 4,
    "masters": 4,
    "m.tech": 4,
    "mtech": 4,
    "m.e": 4,
    "mba": 4,
    "msc": 4,
    "m.sc": 4,

    "bachelor": 3,
    "bachelors": 3,
    "b.e": 3,
    "be": 3,
    "b.tech": 3,
    "btech": 3,
    "b.sc": 3,
    "bsc": 3,
    "bca": 3,
    "bba": 3,

    "diploma": 2,

    "12th": 1,
    "higher secondary": 1,
    "high school": 1
}


def extract_education_level(text):
    """
    Identify the highest education level
    mentioned in the text.
    """

    if not text:
        return 0

    normalized_text = text.lower()

    highest_level = 0

    for education, level in EDUCATION_LEVELS.items():

        if education in normalized_text:

            highest_level = max(
                highest_level,
                level
            )

    return highest_level


# ============================================================
# EDUCATION MATCHING
# ============================================================

def education_match(
    required_education,
    candidate_education
):
    """
    Compare required and candidate education levels.

    Returns:
        100 if candidate meets requirement
        0 otherwise
    """

    if required_education == 0:
        return 100.0

    if candidate_education >= required_education:
        return 100.0

    return 0.0


# ============================================================
# EXPERIENCE MATCHING
# ============================================================

def experience_match(
    required_years,
    candidate_years
):
    """
    Compare required years of experience
    with candidate experience.

    Returns a percentage.
    """

    if required_years <= 0:
        return 100.0

    if candidate_years >= required_years:
        return 100.0

    percentage = (
        candidate_years /
        required_years
    ) * 100

    return round(
        min(percentage, 100.0),
        2
    )