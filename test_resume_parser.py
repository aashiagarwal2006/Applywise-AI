from app.resume_parser import extract_text_from_pdf

text = extract_text_from_pdf("resume.pdf")
print(text[:500])
