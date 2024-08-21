from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
# Create a canvas
c = canvas.Canvas("coordinates1.pdf",pagesize=A4)

c.translate(0,A4[1] ) 
c.setFontSize(10)
for i in range(0,int(A4[1]),12): 
    c.drawString(5,i*-1,f'y: ${str(i*-1)}')


c.save()