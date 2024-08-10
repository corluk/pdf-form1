from reportlab.pdfgen import canvas
from reportlab.lib import colors

# Create a PDF with ReportLab
pdf_file = "example_text_rendering_corrected.pdf"
c = canvas.Canvas(pdf_file)

# Set the font and size
c.setFont("Helvetica", 16)

# Draw normal filled text (default)
c.setFillColor(colors.black)
c.drawString(100, 700, "This is filled text.")

# Stroke text only (outline text)
c.setStrokeColor(colors.red)
c.setLineWidth(1)
c._textRenderMode = 1  # Simulates stroking text
c.drawString(100, 650, "This is stroked text (outline).")
c._textRenderMode = 0  # Reset to fill text

# Fill and stroke text
c.setFillColor(colors.blue)
c.setStrokeColor(colors.green)
c._textRenderMode = 2  # Simulates filling and stroking text
c.drawString(100, 600, "This is filled and stroked text.")

# Save the PDF
c.save()
