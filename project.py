from fpdf import FPDF

pdf = FPDF(orientation='portrait',unit='mm',format='A4')
pdf.add_page()

pdf.set_font(family='Times', size=12)
pdf.cell(w=0, h=10, ln=1, border=1, txt='You making progress bro')
pdf.set_font(family='Times',size=10)
pdf.cell(w=0, h=5, ln=1, border=1,txt='Just keep working hard')
pdf.output('result.pdf')
print(type(pdf))