from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
def points_to_mm(points):
    return points * (25.4 / 72)
class Fonts: 
    def __init__(self):
        self.list = {} 
    def AddFont(self,name , path) : 
        self.list[name] = path
    def ImportFonts(self):

        for key in self.list:
            value = self.list[key]
            pdfmetrics.registerFont(TTFont(key,value))

class PageCoordinates : 
    def __init__(self, pageSize) -> None:
        self.W  , self.H = pageSize 
 
    def GetTopLeft(self): 
        left = self.H * -1
        return self.W, left 


def GetPageSizesAsMM(pagesize):
    w, h = pagesize 
    return points_to_mm(w) , points_to_mm(h)

def GetPointAsMM(point): 
    return points_to_mm(point)  
# Example usage:
a4_width_points, a4_height_points = 595.27, 841.89
a4_width_mm = points_to_mm(a4_width_points)
a4_height_mm = points_to_mm(a4_height_points)