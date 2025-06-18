from fpdf import FPDF
import unicodedata

def sanitize_text(text):
    """
    Normalize Unicode characters to ASCII-safe equivalents.
    This prevents encoding errors with fpdf (which only supports Latin-1).
    """
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")

def export_text_to_pdf(text, filename="tailored_resume.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=11)

    sanitized_text = sanitize_text(text)
    lines = sanitized_text.split("\n")
    for line in lines:
        pdf.multi_cell(0, 10, line)

    pdf.output(filename)
