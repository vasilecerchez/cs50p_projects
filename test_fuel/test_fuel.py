

from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()
    test_two()
    test_zero_diviion()
    test_value_error()



def test_convert():
    assert convert("2/4")==50
    assert convert("3/4")==75
    assert convert("2/3")==67
    assert convert("1/10")==10

    

def test_gauge():
    assert gauge(1)=="E"
    assert gauge(99)=="99%"
    assert gauge(53)=="53%"
    assert gauge(12)=="12%"


def test_two():
    assert convert("2/4")==50 and gauge(50)=="50%"
    assert convert("99/100")==99 and gauge(99)=="99%"
    assert convert("1/100")==1 and gauge(1)=="E"



def test_zero_diviion():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    
def test_value_error():
    with pytest.raises(ValueError):
        convert("a/b")

        
if __name__=="__main__":
    main()