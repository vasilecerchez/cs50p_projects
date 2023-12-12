
"""
Either before or after you implement count in um.py, additionally implement,
in a file called test_um.py, three or more functions that collectively test 
your implementation of count thoroughly, each of whose names should begin with 
test_ so that you can execute your tests with:
"""

from um import count

def main():
    test_count()
    test_count_zero()


def test_count():
    assert count("um")==1
    assert count("um,")==1
    assert count("uM?")==1
    assert count("uM? um ")==2
    assert count("Um, thanks for the album.")==1
    assert count("Um, thanks, um...")==2
    assert count("mistakenly only match an “um” that")==1
    assert count("mistakenly only match an “UM” that")==1
    
def test_count_zero():
    assert count("use correct and incorrect versions")==0
    assert count("should show that all of your")==0
    assert count("umy")==0
    assert count("hello 2024")==0
    
if __name__=="__main__":
    main()   


