from  reportlab.pdfgen.canvas import Canvas  
from .view_base import ViewBase
from reportlab.lib.pagesizes import A4
from enum import Enum
from reportlab.lib import colors
class TrackViewConstants(Enum): 
    FirstYPosition = 215.063
   
    HeightEach = 130.125
    MarginYEach = 8.5  
    MarginX = 15
    CorrectionY = .768

def RenderTrackNo(canvas:Canvas,trackNo:int):
    
    currentShiftY = (trackNo - 1) * (TrackViewConstants.HeightEach.value  + TrackViewConstants.MarginYEach.value)   + ((trackNo -1) * TrackViewConstants.CorrectionY.value)
    shiftByFirstPosition =  TrackViewConstants.FirstYPosition.value +  currentShiftY
    y = A4[1] - shiftByFirstPosition
     
    #canvas.translate(TrackViewConstants.MarginX.value,y)
    canvas.setFillColor(colors.black)
    xy = [TrackViewConstants.MarginX.value , y]
    wh = [TrackViewConstants.MarginX.value,TrackViewConstants.HeightEach.value]
    canvas.rect(xy[0],xy[1],wh[0],wh[1],1,1)
    #canvas.drawString(xy[0],xy[1],"here text ")
    canvas.rotate(90)
    
    canvas.setFillColor(colors.red)
    # this will Y point 
    # from the point of shift to total heigth / 2  
    textMiddleX = xy[1] + (wh[1]/2)
    # X point reversed to Y 
    textMiddleY = xy[0] + (wh[0]/2)
    canvas.drawCentredString(textMiddleY , textMiddleX, "y:" +  str(textMiddleY) +"."+ " x: " + str(textMiddleX))
    canvas.resetTransforms()
    # TODO rotate text 90 on center 
    
 