#import unittest 
import pytest 
from pdfrw import PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black, gray
from .utils import GetPageSizesAsMM , PageCoordinates , Fonts , points_to_mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os 
from reportlab.lib.units import mm
def GetYMargin(margin) : 
    _ , height = A4 
    return (height - margin) 
def GetXMargin(margin): 
    return margin 
def draw_text_in_rectangle(pdf_canvas, text, x, y, w , h ,font , fontsize ):
    """
    Gri arka planlı ve siyah renkli bir metni dikdörtgen içine çizer.
    
    Args:
    pdf_canvas (canvas.Canvas): PDF çizim tuvali.
    text (str): Dikdörtgen içine çizilecek metin.
    x_mm (float): Dikdörtgenin sol alt köşesinin x koordinatı (milimetre cinsinden).
    y_mm (float): Dikdörtgenin sol alt köşesinin y koordinatı (milimetre cinsinden).
    width_mm (float): Dikdörtgenin genişliği (milimetre cinsinden).
    height_mm (float): Dikdörtgenin yüksekliği (milimetre cinsinden).
    """
    
    # Milimetre değerlerini nokta birimine dönüştür
  
   
    # Dikdörtgenin arka plan rengini ayarla
    pdf_canvas.setFillColor(gray)
    pdf_canvas.rect(x, y, w , h, fill=1,stroke=1)

    # Metin rengini ayarla
    pdf_canvas.setFillColor(black)

    # Metni çiz (x ve y koordinatlarını metnin sol alt köşesi olarak ayarla)
    #text_x = x + 5 * mm  # Metni dikdörtgenin içine biraz içeriye al
    #text_y = y + height - 15 * mm  # Metni dikdörtgenin üst kısmından biraz aşağıya al
    
    text_width = pdfmetrics.stringWidth(text, font , fontsize)
    pdf_canvas.setFont(font,fontsize)
    text_margin_x = (w - text_width) /2
    text_margin_x = x + text_margin_x
    text_margin_y = y+1+ (h - fontsize) / 2 
    #text_width = points_to_mm(text_width)
    #margin_x_text = x + ((width_mm - text_width ) / 2) 
    pdf_canvas.drawString(text_margin_x, text_margin_y, text)
def test_iter1_createpdf():
    fonts =  Fonts() 
    current_file_directory = os.path.dirname(__file__) 
    fonts.AddFont("apton-narrow-bold",current_file_directory + "/assets/ApronNarrow-Bold.ttf")
    fonts.ImportFonts()
    page = canvas.Canvas("test1.pdf",pagesize=A4)
    x_mm = GetXMargin(10)
    y_mm = GetYMargin(5)
    coordinates = PageCoordinates(A4)
    imagex_mm = GetXMargin(5)
    imagey_mm= GetYMargin(50)
    w , h = GetPageSizesAsMM(A4)
 
    left,top   = coordinates.GetTopLeft()
    posA = top  +16
    page.setFont("apton-narrow-bold",12)
    #y_mm = 10
    str = f'"x_mm: " {x_mm}  " y_mm:" {y_mm} : Hello, ReportLab!"'
    
    page.drawString(x_mm, y_mm , str )
    imageFile= current_file_directory  + "/assets/image1.jpg"
    page.drawImage(imageFile,imagex_mm,imagey_mm,147,  47)
    #page.drawString(100, h +  297 , "This is a sample PDF.")
    draw_text_in_rectangle(page,"ALBÜM ADI",13,300 ,72, 17,"apton-narrow-bold",12)
    page.save()
""" 
class TestPDF(unittest.TestCase):
    def SimpleReadWrite(): 
        page = canvas.Canvas("test1.pdf",pagesize=A4)
        w , h = A4 
        page.drawString(0,0,"hello world")
        page.save()
"""


    