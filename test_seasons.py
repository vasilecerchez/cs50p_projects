

"""
You’re welcome to import other (built-in) libraries, o
r any that are specified in the below hints. Exit via sys.exit if the user
does not input a date in YYYY-MM-DD format. Ensure that your program will 
not raise any exceptions.

Either before or after you implement seasons.py, additionally implement, in 
a file called test_seasons.py, one or more functions that test your 
implementation of any functions besides main in seasons.py thoroughly, 
each of whose names should begin with test_ so that you can execute your 
tests with:
"""



from seasons import check_date, two_date_time, daystoseconds, numbers_to_words
import pytest



def main():
    test_two_date_time()
    test_daystoseconds()
#    
#def test_check_date():
#    assert check_date("2022-1-1")==None
#    assert check_date("2023-12-5")==None
#    assert check_date("5-10-2020")==None
#    assert check_date("2025-04-05")==None
#    assert check_date("2022-01-01")==True
#    assert check_date("2023-12-05")==True
#    assert check_date("1998-04-07")==True
#    assert check_date("2008-12-31")==True
#
def test_two_date_time():
    assert two_date_time("2020-02-12")==1398
    assert two_date_time("2022-12-24")==352

def test_daystoseconds():
    assert daystoseconds(1398)==2013120
    assert daystoseconds(352)==506880

def test_numbers_to_words():
    assert numbers_to_words(525600)=="Five hundred twenty-five thousand, six hundred"
    
    
if __name__=="__main__":
    main()   