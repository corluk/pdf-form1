from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black, gray


    
class WriteInRect(Page): 
    page : canvas
    width : int 
    height : int 
 
    page_height: int 


    