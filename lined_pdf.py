from fpdf import FPDF
import pandas as pd

def set_footer():
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


def set_lines():
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)


df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()

    #Set the header
    pdf.set_font("Times", "B", 24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], border=0, ln=1, align='L')

    pdf.ln(265)
    set_lines()
    set_footer()

    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.ln(277)
        set_lines()
        set_footer()

pdf.output("lined_pdf.pdf")
