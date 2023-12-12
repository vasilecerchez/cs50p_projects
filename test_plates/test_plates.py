



from plates import is_valid

def main():
    test_words_is_valid()
    test_phrases_is_valid()
    test_phrases_is_valid()
    test_numbers_is_valid()

def test_words_is_valid():
    assert is_valid("ciao")==True
    assert is_valid("C")==False
    assert is_valid("Python")==True
    assert is_valid("cs50")==True
    assert is_valid("csUSA50")==False
    assert is_valid("50CS")==False
    assert is_valid("C5S0")==False
    assert is_valid("")==False
    assert is_valid("50")==False
    assert is_valid("AA")==True
    assert is_valid("B2")==False
    assert is_valid("2A")==False
    assert is_valid("AB12CD")==False
    assert is_valid("ABc012")==False
    

def test_phrases_is_valid():
    assert is_valid("hello CS50")==False
    assert is_valid("hey cs50")==False
    assert is_valid("Me 50")==False

def test_numbers_is_valid():
    assert is_valid("1995")==False
    assert is_valid("one")==True
    assert is_valid("twoone")==True
    
def test_puntuation_is_valid():
    assert is_valid("Bello?")==False
    assert is_valid("one.")==False
    assert is_valid("two,one")==False


if __name__=="__main__":
    main()
