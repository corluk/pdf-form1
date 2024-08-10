from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def create_pdf(file_path):
    # Create a canvas object
    c = canvas.Canvas(file_path, pagesize=A4)
    
    # Create a reusable form (like a stamp or logo)
    c.beginForm("my_form")
    
    # Draw something in the form, like a red square with text
    c.setFillColor(colors.red)
    c.rect(0, 0, 100, 100, fill=True)
    c.setFillColor(colors.white)
    c.setFont("Helvetica", 12)
    c.drawCentredString(50, 50, "LOGO")
    
    # End the form creation
    c.endForm()

    # Now you can "do" this form anywhere on the canvas using translate()
    c.saveState()
    c.translate(100, 700)  # Move the origin to (100, 700)
    c.doForm("my_form")  # Draw the form at the new origin
    c.restoreState()

    c.saveState()
    c.translate(300, 700)  # Move the origin to (300, 700)
    c.doForm("my_form")  # Draw the form at the new origin
    c.restoreState()

    c.saveState()
    c.translate(500, 700)  # Move the origin to (500, 700)
    c.doForm("my_form")  # Draw the form at the new origin
    c.restoreState()

    # You can even scale or rotate the form when placing it
    c.saveState()
    c.translate(100, 500)
    c.scale(2, 2)  # Scale the form to double its size
    c.doForm("my_form")
    c.restoreState()

    c.saveState()
    c.translate(300, 500)
    c.rotate(45)  # Rotate the form by 45 degrees
    c.doForm("my_form")
    c.restoreState()

    # Save the PDF
    c.save()

# Create the PDF
create_pdf("example_with_doForm_corrected.pdf")
