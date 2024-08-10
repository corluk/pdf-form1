from  reportlab.pdfgen.canvas import Canvas 

def CreateAlbumSection(): 

    canvas = Canvas("albumadı.pdf",[595,16])
    canvas.saveState() 
    canvas.setFillColorRGB(0.5, 0.5, 0.5)

    canvas.rect(13.10,0,72.45,15,1,1)
    canvas.setFillColorRGB(0,0,0)
    canvas.translate(13.10,0)
    canvas.drawCentredString(36,3,"ALBÜM ADI")
    
    
    
    canvas.resetTransforms()
    canvas.setFillColorRGB(1,1,1)
    canvas.rect(85.55,0,183.11,15,1,1)
    canvas.setFillColorRGB(0,0,0) 
    canvas.translate(85.55, 0)
    canvas.drawCentredString(95.55,3,"some text in here ") 
    canvas.save()
 
    