from .align import Align , AlignVertical , AlignHorizantal
from reportlab.pdfbase import pdfmetrics
from typing import Callable
from .engine import Engine 
class Container(): 
    _coordinates : tuple[float,float]
    _dimensions : tuple[float,float]
    _max = tuple[float,float]
    _align : Align 
    def __init__(self,w:float,h:float): 
        self._max = [w,h]
        self._align = Align(self._max)
    def GetCoordinates(self): 
        return self._coordinates 
    
    def SetCoordinates(self,x:float,y:float): 
        _x = x 
        _y = self._max[1] -y 
        if _x > self.max[0] : 
            raise "x position exceed width"
        if _y < 1 : 
            raise "y position exceed height" 
        self._coordinates = [_x,_y]
    
    def SetDimensions(self,w:float,h:float): 
        self._dimensions = [w,h]
    def GetDimensions(self):
        return self._dimensions
    def GetAlign(self): 
        return self._align
    def Draw(self):
        raise "not implemented"

class TextContainer(Container):
    _content : str 
    _fontName : str = "Helvetica"
    _fontSize : float = 12 
    def __init__(self, content : str , w: float ,h:float):
        super().__init__(w,h)
        self._content = content
    def SetFontName(self, fontName  : str) : 
        self._fontName = fontName
    def SetFontSize(self,fontSize:float ): 
        self._fontSize = fontSize


    def GetTextDimensions(self):
        w = pdfmetrics.stringWidth(self._content,self._fontName,self._fontSize,"utf8")
        super().SetDimensions([w, self._fontSize + 1 ])
    def DrawText(self,engine : Engine): 
        x, y   = self.GetCoordinates() 
        w , h =  super().GetDimensions()
        canvas = engine.GetCanvas()
        canvas.grid
 
        

