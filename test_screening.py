from src.screening import screen_resume


# ============================================================
# JOB DESCRIPTION
# ============================================================

job_description = """

Python Developer

We are looking for a Python Developer
to join our software development team.

Requirements:

Bachelor's degree in Computer Science
or a related field.

Minimum 2 years of experience.

Required skills:

Python
Django
REST API
MySQL
Git

The candidate should have experience
building backend web applications,
developing APIs and working with databases.

"""


# ============================================================
# RESUME
# ============================================================

resume_path = (
    "data/resumes/test_resume.txt"
)


# ============================================================
# SCREEN CANDIDATE
# ============================================================

result = screen_resume(
    resume_path=resume_path,
    job_description=job_description,
    candidate_name="Pranathi KC"
)


# ============================================================
# DISPLAY RESULT
# ============================================================

print("\n")
print("=" * 70)
print("RESUME SCREENING RESULT")
print("=" * 70)


print(
    f"\nCandidate: "
    f"{result['candidate_name']}"
)

print(
    f"Rank: "
    f"{result.get('rank', 'Not ranked')}"
)


print("\n" + "-" * 70)
print("SCORES")
print("-" * 70)


print(
    f"Skill Match: "
    f"{result['skill_score']}%"
)

print(
    f"Semantic Similarity: "
    f"{result['semantic_score']}%"
)

print(
    f"Experience Match: "
    f"{result['experience_score']}%"
)

print(
    f"Education Match: "
    f"{result['education_score']}%"
)

print(
    f"FINAL SCORE: "
    f"{result['final_score']}%"
)

print(
    f"Recommendation: "
    f"{result['recommendation']}"
)


print("\n" + "-" * 70)
print("SKILL ANALYSIS")
print("-" * 70)


print("\nRequired Skills:")

for skill in result["required_skills"]:

    print(
        f"• {skill}"
    )


print("\nCandidate Skills:")

for skill in result["candidate_skills"]:

    print(
        f"• {skill}"
    )


print("\nMatched Skills:")

for skill in result["matched_skills"]:

    print(
        f"✓ {skill}"
    )


print("\nMissing Skills:")

for skill in result["missing_skills"]:

    print(
        f"✗ {skill}"
    )


print("\n" + "-" * 70)
print("EXPERIENCE")
print("-" * 70)


print(
    f"Required: "
    f"{result['required_experience']} years"
)

print(
    f"Candidate: "
    f"{result['candidate_experience']} years"
)


print("\n" + "-" * 70)
print("EDUCATION")
print("-" * 70)


print(
    f"Required Education Level: "
    f"{result['required_education']}"
)

print(
    f"Candidate Education Level: "
    f"{result['candidate_education']}"
)


print("\n" + "=" * 70)