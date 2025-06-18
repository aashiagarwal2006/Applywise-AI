from app.resume_parser import extract_text_from_pdf
from app.job_scraper import fetch_internships
from app.gpt_utils import generate_cv

resume_text = extract_text_from_pdf("test_resume.pdf")
jobs = fetch_internships(query="data science intern", pages=1)
job_description = jobs[0]["description"]

cv = generate_cv(job_description, resume_text)

print("\n===== Tailored CV Output =====\n")
print(cv)
