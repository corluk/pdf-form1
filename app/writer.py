from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black, gray

class Page: 
    pH :int
    pW : int 
    cX : int 
    cY : int  
    x : int 
    y : int 
    def __init__(self,size : tuple[float,float]): 
        self.pW , self.pH = size 
    def GetMargins(self,x_margin:int,y_margin :int): 
        return [x_margin , (self.pW - y_margin)]
    def SetCurrentX(self,x:int):
        self.cX = x 
    def SetCurrentY(self,y:int):
        self.cY = y 
    
class WriteInRect(Page): 
    page : canvas
    width : int 
    height : int 
 
    page_height: int 


    