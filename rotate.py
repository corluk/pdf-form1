from reportlab.pdfgen import canvas

# Create a canvas
c = canvas.Canvas("rotated_text.pdf")

# Define the rectangle position and size
rect_x = 15
rect_y = 100
rect_width = 10
rect_height = 30

# Calculate the center of the rectangle
center_x = rect_x + rect_width / 2
center_y = rect_y + rect_height / 2

# Save the state of the canvas before rotating
c.saveState()

# Translate to the center of the rectangle
c.translate(center_x, center_y)

# Rotate the canvas by 90 degrees (counter-clockwise)
c.rotate(90)

# Since the coordinate system is rotated, draw the text centered at (0, 0)
c.drawCentredString(0, 0, "Rotated Text")

# Restore the canvas to its original state
c.restoreState()

# Draw the rectangle (optional, for visual reference)
c.rect(rect_x, rect_y, rect_width, rect_height)

# Save the PDF
c.save()

