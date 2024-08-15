from  reportlab.pdfgen.canvas import Canvas  
from .view_base import ViewBase
from reportlab.lib.pagesizes import A4
from enum import Enum
from reportlab.lib import colors
class TrackViewConstants(Enum): 
    FirstYPosition = 214.5
   
    HeightEach = 130
    MarginYEach = 8.5  
    MarginX = 15

def RenderTrackNo(canvas:Canvas,trackNo:int):
    
    currentShiftY = (trackNo - 1) * (TrackViewConstants.HeightEach.value  + TrackViewConstants.MarginYEach.value) 
    y = A4[1] - TrackViewConstants.FirstYPosition.value +  currentShiftY
     
    #canvas.translate(TrackViewConstants.MarginX.value,y)
    canvas.setFillColor(colors.black)
    xy = [TrackViewConstants.MarginX.value , y]
    canvas.rect(xy[0],xy[1],12,130,1,1)
    #canvas.drawString(xy[0],xy[1],"here text ")
    #canvas.rotate(90)
    eserno  = str(trackNo+1)
    canvas.setFillColor(colors.red)
    
    canvas.drawCentredString(xy[0] + 10 , xy[1],eserno +"."+" Eser")

 