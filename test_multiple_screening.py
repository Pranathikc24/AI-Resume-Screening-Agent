from pathlib import Path

from src.screening import screen_multiple_resumes


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
# RESUME DIRECTORY
# ============================================================

resume_directory = Path(
    "data/resumes"
)


# ============================================================
# FIND ALL PDF RESUMES
# ============================================================

resume_paths = sorted(
    resume_directory.glob("*.pdf")
)


print("\n")
print("=" * 80)
print("AI RESUME SCREENING AGENT")
print("=" * 80)

print(
    "\nJob Role: Python Developer"
)

print(
    f"PDF Resumes Found: "
    f"{len(resume_paths)}"
)


# ============================================================
# CHECK WHETHER RESUMES EXIST
# ============================================================

if not resume_paths:

    print(
        "\nNo PDF resumes found."
    )

    print(
        "\nPlease place PDF resumes inside:"
    )

    print(
        "data/resumes/"
    )

    exit()


print("\nPDF Files:")

for path in resume_paths:

    print(
        f"  • {path.name}"
    )


# ============================================================
# SCREEN ALL RESUMES
# ============================================================

print("\n")
print("=" * 80)
print("SCREENING CANDIDATES...")
print("=" * 80)


results = screen_multiple_resumes(
    resume_paths=resume_paths,
    job_description=job_description
)


# ============================================================
# DISPLAY FINAL RANKING
# ============================================================

print("\n")
print("=" * 80)
print("FINAL CANDIDATE RANKING")
print("=" * 80)


for candidate in results:

    print(
        f"\n#{candidate['rank']} "
        f"{candidate['candidate_name']}"
    )

    print(
        f"   Skill Match: "
        f"{candidate['skill_score']}%"
    )

    print(
        f"   Semantic Similarity: "
        f"{candidate['semantic_score']}%"
    )

    print(
        f"   Experience Match: "
        f"{candidate['experience_score']}%"
    )

    print(
        f"   Education Match: "
        f"{candidate['education_score']}%"
    )

    print(
        f"   FINAL SCORE: "
        f"{candidate['final_score']}%"
    )

    print(
        f"   Recommendation: "
        f"{candidate['recommendation']}"
    )

    print(
        f"   Matched Skills: "
        f"{', '.join(candidate['matched_skills'])}"
    )

    print(
        f"   Missing Skills: "
        f"{', '.join(candidate['missing_skills'])}"
    )


# ============================================================
# COMPLETION
# ============================================================

print("\n")
print("=" * 80)
print("SCREENING COMPLETED")
print("=" * 80)