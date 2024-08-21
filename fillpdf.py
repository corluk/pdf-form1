from pdfrw import PdfReader, PdfWriter, PageMerge,PdfDict
def fill_pdf(input_pdf, output_pdf, data_dict):
    template_pdf = PdfReader(input_pdf)
    
    for page in template_pdf.pages:
        annotations = page['/Annots']
        if annotations:
            for annotation in annotations:
                field = annotation.get('/T')
                if field:
                    key = field.to_unicode()
                    if key in data_dict:
                        annotation.update(
                            PdfDict(V=data_dict[key])  # Ff=1 ensures field is read-only after filling
                        )
    PdfWriter(output_pdf, trailer=template_pdf).write()

# Example usage
input_pdf = './app/fonts/source.pdf'  # Replace with your PDF file
output_pdf = 'output_filled2.pdf'  # Replace with your desired output file name
keys  = {}
with open('fields.txt', 'r' , encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        value = line.strip()
        keys[value] = value.upper()
        
data_dict = {
    'fill_71': 'Value1',
    'FieldName2': 'Value2',
}
print(keys)

fill_pdf(input_pdf, output_pdf, keys)