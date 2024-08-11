from  reportlab.pdfgen.canvas import Canvas 
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from io import BytesIO
import os 
def WriteBottomText():
    current_file_directory = os.path.dirname(__file__)  
    font = pdfmetrics.registerFont(TTFont("calibri-regular",current_file_directory + "/fonts/Calibri Regular.ttf"))

    text = """ 
    İşbu form; bu formda ismi ve imzası bulunan MÜYORBİR üyesinin, imzaladığı Yetki Belgesinin bir eki ve ayrılmaz bir parçasıdır. İş bu formda tanımı yapılan 
    icraların yorum haklarının sahibi bulunduğumu, bu icralardaki haklarımı yetki belgesine bağlı olarak MÜYORBİR'e devrettiğimi kabul ve beyan ederim.
    """
    file = BytesIO()
    c = Canvas(file ,[307,68])
    
    c.setFillColorRGB(.5,.5,.5)
    c.rect(0,0,307,68,0,1) 
    
    x = 0 
    y = 0 
    styles = getSampleStyleSheet()
    c.setFillColorRGB(0,0,0)
    style = ParagraphStyle(
    name='CenterStyle',
    parent=styles['BodyText'],
    alignment=1,  # 1 for center alignment
    fontSize=7.8,
    leading=7,  # line height
    spaceAfter=7,
    fontName="calibri-regular"
    )
    width = 250
    height = 68
    paragraph = Paragraph(text, style)
    w, h = paragraph.wrap(width, height)
    text_x =  (307 -250)/2
    text_y = h - 5
   
    paragraph.drawOn(c,text_x,text_y)
    c.save()
    file.seek(0)
    return file 