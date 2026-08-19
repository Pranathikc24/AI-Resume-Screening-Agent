from src.parser import extract_resume_text

from src.profile import (
    extract_years_of_experience,
    extract_education_level,
    experience_match,
    education_match
)


# ============================================================
# LOAD RESUME
# ============================================================

resume_file = "data/resumes/test_resume.txt"

resume_text = extract_resume_text(
    resume_file
)


# ============================================================
# TEST RESUME EXTRACTION
# ============================================================

candidate_experience = extract_years_of_experience(
    resume_text
)

candidate_education = extract_education_level(
    resume_text
)


print("=" * 70)
print("CANDIDATE PROFILE")
print("=" * 70)

print(
    f"\nCandidate Experience: "
    f"{candidate_experience} years"
)

print(
    f"Candidate Education Level: "
    f"{candidate_education}"
)


# ============================================================
# TEST JOB DESCRIPTION
# ============================================================

job_description = """
Python Developer

Requirements:

Bachelor's degree in Computer Science
or a related field.

Minimum 2 years of experience.

Strong experience in Python,
Django, REST API and MySQL.
"""


# ============================================================
# EXTRACT JD REQUIREMENTS
# ============================================================

required_experience = extract_years_of_experience(
    job_description
)

required_education = extract_education_level(
    job_description
)


print("\n" + "=" * 70)
print("JOB REQUIREMENTS")
print("=" * 70)

print(
    f"\nRequired Experience: "
    f"{required_experience} years"
)

print(
    f"Required Education Level: "
    f"{required_education}"
)


# ============================================================
# CALCULATE MATCH
# ============================================================

experience_score = experience_match(
    required_experience,
    candidate_experience
)

education_score = education_match(
    required_education,
    candidate_education
)


print("\n" + "=" * 70)
print("MATCH RESULTS")
print("=" * 70)

print(
    f"\nExperience Match: "
    f"{experience_score}%"
)

print(
    f"Education Match: "
    f"{education_score}%"
)