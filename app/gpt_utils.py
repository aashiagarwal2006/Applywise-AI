import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # <-- This line was missing

def generate_full_resume(job_description, resume_text):
    prompt = f"""
You are a professional AI resume editor.

Given the following:
- Job description for an internship: {job_description}
- Candidate's full resume content: {resume_text}

Return:
1. A 1-page resume, tailored and reordered to best match the job.
2. It should sound polished, use bullet points, and prioritize experiences relevant to the job.
3. Trim unrelated items. Use strong, action-oriented phrasing.

Format your output with clear section titles (Education, Experience, Projects, Skills).

Start directly with the resume content. Do not include any notes or explanation.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or gpt-4 if available
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content

def generate_cv(job_description, resume_text):
    prompt = f"""
You are an AI career assistant.

Using the full resume content below, and tailoring it to the job description, generate a **2+ page CV** that includes all relevant projects, experiences, and skills. Keep it highly detailed and well-structured.

Job Description:
{job_description}

Candidate Resume:
{resume_text}

Format the CV with clear section titles: Education, Experience, Projects, Publications, Skills, and Other (if needed).

Start directly with the CV content.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content
