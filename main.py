from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import gray , black

def create_pdf_with_form_and_image(output_filename, image_path):
    # Create a canvas object
    c = canvas.Canvas(output_filename, pagesize=A4)
    width, height = A4
    
    # Add an image
    c.drawImage(image_path, 50, height - 200, width=100, height=100)
    
    # Add form fields
    form = c.acroForm
    
    # Adding labels with gray background for fields
    labels = [
        ("YAPIT ADI:", 20, height - 250),
        ("YORUMCU ADI:", 20, height - 280),
        ("SÖZ YAZARI:", 20, height - 310)
    ]
    
    for text, x, y in labels:
        # Draw gray background rectangle
        c.setFillColor(gray)
        c.rect(x - 5, y , 100, 20, fill=1)
        # Draw the label text
        c.setFillColor(black)
        c.drawString(x, y, text)
    
    # Adding text fields
    form.textfield(name='YAPIT_ADI_2', x=100, y=height - 250, width=200, height=20, borderColor=black)
    form.textfield(name='YORUMCU_ADI', x=100, y=height - 280, width=200, height=20, borderColor=black)
    form.textfield(name='SÖZ_YAZARI', x=100, y=height - 310, width=200, height=20, borderColor=black)
    # Continue adding other fields as needed...
    
    # Finalize the PDF
    c.save()

# Path to the image you want to add
image_path = 'img1790.jpg'

# Create the PDF with form fields and an image
create_pdf_with_form_and_image('output_with_form_and_image.pdf', image_path)
