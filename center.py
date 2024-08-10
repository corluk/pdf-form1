from reportlab.pdfgen import canvas
from reportlab.lib import colors

# Create a PDF with ReportLab
pdf_file = "example_centered_text.pdf"
c = canvas.Canvas(pdf_file)

# Set the font and size
c.setFont("Helvetica", 16)

# Set the text color to black
c.setFillColor(colors.black)

# Define the coordinates for the text
x = 300  # x-coordinate (horizontal center point)
y = 500  # y-coordinate (vertical position)

# Draw centered text
c.drawCentredString(x, y, "This text is centered at x=300")

# Save the PDF
c.save()
