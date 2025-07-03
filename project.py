from fpdf import FPDF
import pandas as pd
pdf = FPDF(orientation='portrait',unit='mm',format='A4')
pdf.set_auto_page_break(False)
df = pd.read_csv('topicss.csv')
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times',style='B', size=12)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=10, ln=1, border=0, txt=row['Topic'])
    pdf.line(10,22,200,22)
    #set the footer
    pdf.ln(265)
    pdf.set_font(family='Times',style='B',size=4)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,txt=row['Topic'],align='R')
    for x in range(row['Pages']-1):
        pdf.add_page()
        #set the footer
        pdf.ln(275)
        pdf.set_font(family='Times',style='B',size=4)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0,h=10,txt=row['Topic'],align='R')
pdf.output('result.pdf')
