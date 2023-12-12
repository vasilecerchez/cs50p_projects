


from bank import value



def test_letters_bank():
    assert value("h")==20
    assert value("v")==100
    assert value("c")==100
    
def test_world_bank():
    assert value("hello")==0
    assert value("HELLo")==0
    assert value("hi")==20
    assert value("hey")==20
    assert value("Hey")==20
    

def test_phrases_bank():
    assert value("hello world")==0
    assert value("hi guys")==20
    assert value("hey people")==20
    assert value("ciao a tutti")==100
    
    
    
        