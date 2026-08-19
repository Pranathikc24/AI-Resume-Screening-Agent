from src.parser import extract_resume_text


file_path = "data/resumes/test_resume.txt"

text = extract_resume_text(file_path)

print("=" * 60)
print("EXTRACTED RESUME TEXT")
print("=" * 60)

print(text)

print("=" * 60)
print("PARSER TEST COMPLETED")
print("=" * 60)