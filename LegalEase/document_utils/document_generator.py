from docx import Document
from docx.shared import Pt
from fpdf import FPDF


def create_docx(text, filename):
    document = Document()

    style = document.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(12)

    for paragraph in text.split("\n"):
        document.add_paragraph(paragraph)

    document.save(filename)


def create_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=12)

    for line in text.split("\n"):
        pdf.multi_cell(0, 8, line)

    pdf.output(filename)


def create_txt(text, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)