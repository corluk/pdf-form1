from .engine import Engine 
from .page import Page
from reportlab.pdfbase import pdfmetrics
from .container import  Container
class Text():   
    _content : str
    _size = tuple[float,float] 
    _container = Container 
    def __init__(self,content : str  , font : str , fontsize : float = 12  ) -> None:
        self._content = content
        self._font = font 
        self._fontsize = fontsize

    
    def GetContainer(self): 
        w, h = self.GetDimensions() 
        return Container(w,h)  
        
    def GetDimensions(self)-> tuple[float,float]: 
        w = pdfmetrics.stringWidth(self._content,self._font,self._fontsize) 
        h = self._fontsize +1 #correction 
        return [w,h]
    def Draw(self, x, y  ):
        container = self.GetContainer()
        container.SetCoordinates(x,y)
        container.
        position = page.SetPointer(x,y) 
        pdfmetrics.stringWidth(self._content,font,fontsize
                               )
        self._canvas.drawString()   
        