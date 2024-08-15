from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf_form(filename):
    # Create the PDF document
    doc = SimpleDocTemplate(filename, pagesize=letter)
    
    # Sample styles for the document
    styles = getSampleStyleSheet()
    
    # Title of the form
    title = Paragraph("User Information Form", styles['Title'])
    
    # Spacer between elements
    spacer = Spacer(1, 12)
    
    # Form Fields
    data = [
        ['Name:', '____________________________'],
        ['Email:', '____________________________'],
        ['Phone:', '____________________________'],
        ['Address:', '____________________________'],
        ['City:', '____________________________'],
        ['State:', '____________________________'],
        ['Zip Code:', '____________________________'],
    ]
    
    # Create a table with the form fields
    table = Table(data, colWidths=[100, 400])
    
    # Style the table
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    # Build the PDF
    elements = [title, spacer, table]
    doc.build(elements)

# Usage
create_pdf_form("user_information_form.pdf")