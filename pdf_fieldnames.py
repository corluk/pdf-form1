from pdfrw import PdfReader
def get_field_names(input_pdf):
    pdf = PdfReader(input_pdf)
    field_names = set()

    for page in pdf.pages:
        annotations = page['/Annots']
        if annotations:
            for annot in annotations:
                field = annot.get('/T')
                if field:
                    field_names.add(field.to_unicode())

    return field_names
# Example usage
input_pdf = './app/fonts/source.pdf'  # Replace with your PDF file
fields = get_field_names(input_pdf)

 
for field in fields:
    print(field)

    