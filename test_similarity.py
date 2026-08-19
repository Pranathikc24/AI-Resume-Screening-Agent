from src.similarity import similarity_percentage


# ============================================================
# TEST 1
# ============================================================

job_description = """
We are looking for a Python developer with experience
in building REST APIs and backend applications.
The candidate should have experience with databases
and web development.
"""


resume = """
Developed backend applications using Python.
Built RESTful web services and worked with databases.
Experienced in web application development.
"""


score = similarity_percentage(
    job_description,
    resume
)


print("=" * 70)
print("SEMANTIC SIMILARITY TEST")
print("=" * 70)

print(f"\nSimilarity Score: {score}%")