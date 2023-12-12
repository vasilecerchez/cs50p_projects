

"""
Either before or after you implement validate in numb3rs.py, 
additionally implement, in a file called test_numb3rs.py, two or more functions 
that collectively test your implementation of validate thoroughly, 
each of whose names should begin with test_ so that you can execute your 
tests with:"""

from numb3rs import validate


def main():
    test_worlds_validate()  
    test_numbers_validate()
    test_no_numbers_validate()

def test_worlds_validate():
    assert validate("cat")==False
    assert validate("dog")==False
    assert validate("cat")==False
    assert validate("a.b.c.d")==False
    assert validate("a..b.c")==False
    
def test_numbers_validate():
    assert validate("0.0.0.0")==True
    assert validate("255.255.255.255")==True
    assert validate("256.256.256.256")==False
    assert validate("257.257.257.257")==False
    assert validate("512.1.2.255")==False
    assert validate("1.512.2.255")==False
    assert validate("1.2.512.255")==False
    assert validate("1.2.3.512")==False
    assert validate("-1.0.1.2")==False
    assert validate("255")==False
    assert validate("255.")==False   
    assert validate("255.1")==False 
    assert validate("255.1.6.")==False  
    
    
def test_no_numbers_validate():
    assert validate("1.2..3")==False
    assert validate(".2.3.4")==False
    assert validate("...")==False
    
if __name__=="__main__":
    main()   


