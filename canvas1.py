from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
# Create a canvas
c = canvas.Canvas("translated_example.pdf",pagesize=A4)

# Translate the origin to (100, 50)
c.translate(0, A4[1])

# Now, draw a rectangle at (0, 0) relative to the new origin
c.rect(10, -105, 200, 100)  # This will actually be drawn at (100, 50) in the original coordinate system

# Draw some text relative to the new origin
c.drawString(10, -75, "This text is relative to the new origin at (10, -75)")
c.saveState()
c.resetTransforms()
c.translate(0,0) 
c.drawString(10, 841-75,"expected to be in over 75 to bottom")

c.restoreState()

c.drawString(10,-150,"expected to be in y 150 (under 150 to top)")
# Save the PDF
c.save()