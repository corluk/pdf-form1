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
    def GetPosition()