# Modelo de relatório PDF

from fpdf import FPDF
from datetime import datetime

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.set_margins(0,0,0)
pdf.set_line_width(.5)
pdf.line(10,10,200,10)
pdf.line(10,10,10,286)
pdf.line(10,286,200,286)
pdf.line(200,10,200,286)
pdf.text(15,20,txt='Exemplo de PDF!')
data_e_hora_atuais = datetime.now()
data_hora_em_texto = data_e_hora_atuais.strftime("%d-%m-%Y %Hh%M")
pdf.output(data_hora_em_texto + ".pdf")