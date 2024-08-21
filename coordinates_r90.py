from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
# Create a canvas
c = canvas.Canvas("coordinates_r90.pdf",pagesize=A4)
c.rotate(90)
c.translate(A4[1],0) 
c.setFontSize(10)
for i in range(0,int(A4[1]),12): 
    c.drawString(-48,i*-1,f'y: ${str(i*-1)}')


c.save()