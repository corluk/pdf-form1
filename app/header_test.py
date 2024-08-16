import pytest 
from reportlab.pdfgen.canvas import Canvas 
from reportlab.lib.pagesizes import A4
from .header import CreateAlbumSection
from .bottom1 import WriteBottomText
from pypdf import PdfReader, PdfWriter  , PageObject
from io import BytesIO
from .views.track import RenderTrackNo
def createBaseA4(): 
    file = BytesIO()
    c = Canvas(file,A4) 
    c.showPage()
    c.save()
    file.seek(0)
    return file 
def test_header1(): 
    CreateAlbumSection() 

def test_bottom1(): 
    WriteBottomText()

def test_merge() : 
    baseFile = createBaseA4()
    file1 = CreateAlbumSection()
    file2 = WriteBottomText() 
    
    basePdf = PdfReader(baseFile)
    pdfTop = PdfReader(file1)
    pdfBottom = PdfReader(file2)
    writer  = PdfWriter()
   
    basePage =basePdf.pages[0]
    topPage = pdfTop.pages[0]
    bottomPage = pdfBottom.pages[0]
    top_page_content = PageObject.create_blank_page(width=basePage.mediabox.width, height=basePage.mediabox.height)
    top_page_content.merge_page(topPage)
    w, h = A4 
    top_page_content.add_transformation([1, 0, 0, 1, 15, h - 70])
    basePage.merge_page(top_page_content)
    

    bottomContent = PageObject.create_blank_page(width=basePage.mediabox.width,height=basePage.mediabox.height)
    bottomContent.merge_page(bottomPage)
    bottomContent.add_transformation([1,0,0,1,15,h-700])
    basePage.merge_page(bottomContent)
    #basePage.mer(topPage,15,70)

    #basePage.merge_transformed_page(bottomPage,15,700)
   
    writer.add_page(basePage)
    """ 
    topPage = pdfTop.pages[0]
    bottomPage = pdfBottom.pages[0]
    merger = PageMerge(basePdf.pages[0])
    
    m1 = merger.add(pdfTop.pages[0],transform=[1, 0, 0, 1, 15, 70])
    m1.render()
    
    m1 = merger.add(pdfTop.pages[0],viewrect=(0, 0, 1, 1), transform=[1, 0, 0, 1, 15, 800-70])
    
    #m1.ctm = [1, 0, 0, 1, 15, 800-70] 
    m1.render()
    m2 = merger.add(pdfTop.pages[0])
    m2.ctm = [1, 0, 0, 1, 15, 800-700] 
    m2.render()
    output_fp= BytesIO()
    writer = PdfWriter()
    writer.addPage(basePdf.pages[0])
    writer.write(output_fp)
 
    output_fp.seek(0)
    """
    output_fp = BytesIO()
    writer.write(output_fp)
    output_fp.seek(0)
    with open("render1.pdf","wb") as f: 
        f.write(output_fp.read())


def test_track():
    canvas = Canvas("test_track1.pdf",A4)
    RenderTrackNo(canvas=canvas,trackNo=1)
    RenderTrackNo(canvas=canvas,trackNo=2)
    RenderTrackNo(canvas=canvas,trackNo=3)
    RenderTrackNo(canvas=canvas,trackNo=4)
    #RenderTrackNo(canvas=canvas,trackNo=4)
    #RenderTrackNo(canvas=canvas,trackNo=5)
    canvas.save()
