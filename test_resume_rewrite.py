from app.resume_parser import extract_text_from_pdf
from app.job_scraper import fetch_internships
from app.gpt_utils import generate_full_resume
from app.docx_export import export_resume_to_docx
from app.pdf_export import export_text_to_pdf
from app.docx_template_export import export_structured_resume  # ✅ NEW

# Step 1: Extract resume text
resume_text = extract_text_from_pdf("resume.pdf")

# Step 2: Fetch job descriptions (internship)
jobs = fetch_internships(query="software engineering intern", pages=1)
job_description = jobs[0]["description"]  # Use first job description for testing

# Step 3: Generate tailored resume
formatted_resume = generate_full_resume(job_description, resume_text)

# Step 4: Save as raw DOCX (basic version)
export_resume_to_docx(formatted_resume, "tailored_resume.docx")

# Step 5: Save as PDF (basic unformatted)
export_text_to_pdf(formatted_resume, "tailored_resume.pdf")

# Optional: print output
print(formatted_resume)

# ✅ Step 6: Structured DOCX formatting
structured_data = {
    "name": "Aashi Agarwal",
    "email": "aashia3@illinois.edu",
    "linkedin": "linkedin.com/in/aashiagarwal2006",
    "education": [
        "B.S. in Information Science & Data Science, University of Illinois at Urbana-Champaign (Expected May 2027)",
        "Minor in Computer Science",
        "Relevant Coursework: Data Structures, Algorithms, ML, NLP"
    ],
    "experience": [
        {
            "title": "Software Engineering Intern – Lynk (May 2025 – Aug 2025)",
            "bullets": [
                "Worked on software/hardware systems for satellites",
                "Built tooling to support space communications network"
            ]
        },
        {
            "title": "Product & Data Intern – Honeycomb Maps (May 2024 – Aug 2024)",
            "bullets": [
                "Analyzed competitors and VC-backed companies",
                "Integrated LLMs with LlamaIndex & Neo4j for PDF insights",
                "Led pricing strategy using user interviews"
            ]
        }
    ],
    "projects": [
        {
            "title": "AI Resume Rewriter",
            "bullets": [
                "Built GPT-powered app that generates tailored resumes",
                "Used Streamlit + OpenAI API + PDF parsing"
            ]
        }
    ],
    "skills": [
        "Python, Pandas, SQL, Flask, Streamlit, GPT-4, Tableau"
    ]
}

export_structured_resume(structured_data, "tailored_resume_final.docx") 