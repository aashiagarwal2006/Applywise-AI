Applywise-AI 🎯
A lightweight AI agent that scrapes real software engineering internships and rewrites resumes tailored to each role using GPT-3.5. Designed to help students apply smarter, faster.

🚀 Demo
https://youtu.be/76MRK-kFVCs

🛠️ Tech Stack
- Python
- OpenAI GPT-3.5 (via openai Python SDK)
- PyMuPDF (fitz) – PDF parsing
- fpdf – PDF generation (basic formatting)
- python-docx – DOCX export
- JSearch API – for scraping real job listings

🧠 What It Does
- Upload a full resume (PDF format)
- Scrape ~100 real software engineering internship listings using JSearch
- Automatically match the first job and extract its description
- Use GPT-3.5 to rewrite the resume to emphasize relevant experience for that job
- Export the new resume as a .pdf and .docx

✨ Why This Matters
Tailoring a resume for every internship is exhausting — but often necessary. Applywise-AI uses LLMs to automate this process, helping students craft job-specific applications in seconds. It ensures your most relevant projects, experience, and skills are brought to the front — increasing your chances of getting noticed.

📐 Design Choices, Tech Stack & Algorithms
Applywise-AI is built to be modular and efficient for local use.

Module	Purpose
- job_scraper.py	Scrapes internships via the JSearch API
- resume_parser.py	Parses the uploaded PDF and extracts clean text
- gpt_utils.py	Sends job + resume text to GPT-3.5 and formats the rewritten resume
- docx_export.py	Exports the new resume in a clean Word format
- pdf_export.py	Exports the new resume in a PDF format (basic)
- test_resume_rewrite.py	Main test script to run agent end-to-end

⏳ What I'd Improve With More Time
With more time and resources, I would evolve Applywise-AI into a full-service internship application assistant. Key planned features include:
- Cover Letter Generation
  Automatically generate role-specific cover letters alongside tailored resumes.
- Style-Preserving PDF Output
  Maintain original fonts, layout, and formatting for professional polish.
- LinkedIn & GitHub Parsing
  Pull relevant skills, achievements, and experience from public profiles to enhance resume content.
- Application Autofill & Submission Support
  Auto-populate internship application forms and generate review-ready cover letters — streamlining the entire application pipeline from resume to submission.

📂 How to Run Locally
bash
Copy
Edit
git clone https://github.com/aashiagarwal2006/Applywise-AI
cd Applywise-AI
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python test_resume_rewrite.py
