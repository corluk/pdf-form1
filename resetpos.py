from reportlab.pdfgen import canvas

c = canvas.Canvas("example.pdf")

# Draw some text at the initial position
c.drawString(100, 750, "Text at the initial position.")

# Reset position by moving the origin
#c.translate(0, -100)  # Move down by 100 units

# Draw text at the new position
c.drawString(100, 750, "Text after position reset.")

c.save()
