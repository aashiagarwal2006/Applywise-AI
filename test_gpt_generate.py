from app.resume_parser import extract_text_from_pdf
from app.job_scraper import fetch_internships
from app.gpt_utils import generate_application_content

# Load resume text
resume_text = extract_text_from_pdf("resume.pdf")

# Get one job description
jobs = fetch_internships(query="data science intern", pages=1)
sample_job = jobs[0]["description"]

# Run GPT
result = generate_application_content(sample_job, resume_text)

print(result)
