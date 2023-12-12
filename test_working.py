
"""
Either before or after you implement convert in working.py, 
additionally implement, in a file called test_working.py, three or more 
functions that collectively test your implementation of convert thoroughly,
each of whose names should begin with test_ so 
that you can execute your tests with:
"""

from working import convert
import pytest

def main():
    test_convert_ok()
    test_parse_60_min()
    test_convert_input_error()

def test_convert_ok():
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM")=="09:00 to 17:00"
    assert convert("10 PM to 8 AM")=="22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM")=="22:30 to 08:50"
    

    
def test_parse_60_min():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    
def test_convert_input_error():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    
    
    
if __name__=="__main__":
    main()   


