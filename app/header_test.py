import pytest 
from .header import CreateAlbumSection
from .bottom1 import WriteBottomText

def test_header1(): 
    CreateAlbumSection() 

def test_bottom1(): 
    WriteBottomText()