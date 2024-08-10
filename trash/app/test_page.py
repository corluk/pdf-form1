from .page import Page 
from reportlab.lib.pagesizes import A4

def test_should_page_pointer_changes_with_new_values(): 
    p= Page(A4) 
    actualX , actualY = p.SetPointer(10,10) 
    sizeX , sizeY   = A4 
    expectedX  = 10

    expectedY = sizeY - 10 
    assert  actualX == expectedX  
    assert actualY == expectedY
    actualY = p.SetPointerY(20)
    expectedY = expectedY - 20 
    assert actualY == expectedY

