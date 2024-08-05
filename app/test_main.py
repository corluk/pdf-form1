#import unittest 
import pytest 
from pdfrw import PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black, gray
from .utils import GetPageSizesAsMM , PageCoordinates , Fonts 
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os 

 
def test_iter1_createpdf():
    fonts =  Fonts() 
    current_file_directory = os.path.dirname(__file__) 
    fonts.AddFont("apton-narrow-bold",current_file_directory + "/assets/ApronNarrow-Bold.ttf")
    fonts.ImportFonts()
    page = canvas.Canvas("test1.pdf",pagesize=A4)
    
    coordinates = PageCoordinates(A4)

    w , h = GetPageSizesAsMM(A4)
   
    left,top   = coordinates.GetTopLeft()
    posA = top  +16
    page.setFont("apton-narrow-bold",12)
    page.drawString(100, posA*-1 , "Hello, ReportLab!")
    page.drawString(100, h +  297 , "This is a sample PDF.")
    page.save()
""" 
class TestPDF(unittest.TestCase):
    def SimpleReadWrite(): 
        page = canvas.Canvas("test1.pdf",pagesize=A4)
        w , h = A4 
        page.drawString(0,0,"hello world")
        page.save()
"""