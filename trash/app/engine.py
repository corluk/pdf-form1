from .page import Page 
from reportlab.pdfgen.canvas import Canvas
class  Engine(): 
    _engine : Canvas 
    _page : Page  
    _filename: str 
    def __init__(self,fileName : str ,  pageSize : tuple[float,float]):
        self._page = Page(pageSize)
        self._engine=  Canvas(fileName,pageSize)
    def GetCanvas(self) -> Canvas: 
        return self._engine()