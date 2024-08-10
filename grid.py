from reportlab.pdfgen import canvas

# Create a PDF with ReportLab
pdf_file = "example_with_grid.pdf"
c = canvas.Canvas(pdf_file)

# Define grid parameters
x_start = 100
y_start = 500
x_end = 400
y_end = 700

# Define the number of rows and columns
rows = 5
columns = 5

# Draw the grid
c.grid([x_start, x_start + 50, x_start + 100, x_start + 150, x_start + 200, x_end],
       [y_start, y_start + 50, y_start + 100, y_start + 150, y_start + 200, y_end])

# Add some text inside the grid cells
for i in range(rows):
    for j in range(columns):
        x = x_start + 10 + (j * 50)
        y = y_start + 10 + (i * 50)
        c.drawString(x, y, f"Cell {i+1},{j+1}")

# Save the PDF
c.save()