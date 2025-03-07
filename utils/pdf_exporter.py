from fpdf import FPDF, HTMLMixin
from datetime import datetime
import os


class PDFReport(FPDF, HTMLMixin):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.set_margins(15, 20, 15)

    def header(self):
        pass  

    def footer(self):
        pass  

    def add_content(self, title, content):
        self.set_font("Times", "B", 16)
        self.cell(0, 10, title, ln=True)
        self.ln(5)

        self.set_font("Times", "", 12)
        self.multi_cell(0, 8, content, align='J')
        self.ln(10)

    def add_citations(self, citations):
        self.set_font("Times", "B", 16)
        self.cell(0, 10, "Citations", ln=True)
        self.ln(5)

        self.set_font("Times", "", 12)
        for idx, citation in enumerate(citations, 1):
            start = citation.find("http")
            url = citation[start:].strip() if start != -1 else ""

            if url:
                text_before_url = citation[:start].strip()
                self.write(8, f"{idx}. {text_before_url} ")
                self.write(8, url, url)
                self.ln(8)
            else:
                self.write(8, f"{idx}. {citation}")
                self.ln(8)


def generate_pdf(answer, citations, filename="research_report.pdf"):
    pdf = PDFReport()
    pdf.add_page()

    pdf.add_content("Final Answer", answer)
    pdf.add_citations(citations)

    output_path = os.path.join("outputs", filename)
    os.makedirs("outputs", exist_ok=True)
    pdf.output(output_path)

    return output_path
