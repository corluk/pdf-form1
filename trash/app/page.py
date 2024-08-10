from reportlab.pdfgen import canvas
from enum import Enum 
from reportlab.pdfbase.pdfmetrics import stringWidth 
class AlignVertical(Enum):
    LEFT = "left"
    RIGHT = "right" 
    MIDDLE = "middle"

class AlignHorizantal(Enum):
    TOP = "top"
    BOTTOM = "bottom"
    MIDDLE =  "middle"

class Align(): 
    _container   : tuple[float,float] 
    
    _aling : tuple[AlignVertical,AlignHorizantal]

    def __init__(self,size:tuple[float,float]):
        self._container = size 
    
class Page: 
    _pageSize : tuple[float,float]
    _pointerPosition : tuple[float,float]
     
   
    def __init__(self,size : tuple[float,float]): 
        self._pW , self._pH = size 
        self._pointerPosition = [0,0]
        
    def CalculateMargins(self,x_margin:float,y_margin :float) -> tuple[float,float]: 
        w, h = self._pageSize
    
        return [x_margin , h-y_margin]
    
    def ResetX(self) -> float: 
        
        self._pointerPosition  = [0,self._pointerPosition[1]] 
        return self._pointerPosition
    

    def ResetY(self) -> float : 
        self._pointerPosition = [self._pointerPosition[0],0]
        return self._pointerPosition
    def checkX(self,x : float):
        if x > self._pageSize[0] : 
            raise "x position exceed page width" 
    def checkY(self,y: float ):
        if y < 1 : 
            raise "y position excedd page height"

    def SetPointerX(self,x:int) -> float:
        px, _  = self._pointerPosition
        _x = px + x 
        self.checkX(_x)
        self._pointerPosition = [_x,self._pointerPosition[1]]
        return self._pointerPosition
    
    def SetPointerY(self,y:int) -> float:
        _ , py = self._pointerPosition
        _ , h = self._pageSize  
        _y =h - py  
        self.checkY(_y)
        self._pointerPosition = [self._pointerPosition[0],_y]
        return self._pointerPosition
    
    def SetPointer(self,x:float, y : float  ) -> tuple[float,float]: 
        return  [self.SetPointerX(x), self.SetPointerY(y)]  
    
    def ResetAll(self)-> tuple[float,float]:
        return [self.ResetX(), self.ResetY()]


    