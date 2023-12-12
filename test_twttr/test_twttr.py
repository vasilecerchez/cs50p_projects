

from twttr import shorten

def main():
    test_words_shorten()
    test_phrases_shorten()    
    

def test_words_shorten():
    assert shorten("cIao")=="c"
    assert shorten("vasile")=="vsl"

def test_phrases_shorten():
    assert shorten("hello CS50. How are you?")=="hll CS50. Hw r y?"
    assert shorten("my name is giovanni giorgio but everybody calls me giorgio")=="my nm s gvnn grg bt vrybdy clls m grg"

def test_numbers_shorten():
    assert shorten("2024")=="2024"
    assert shorten("Two")=="Tw"

def test_symbols_shorten():
    assert shorten("?:!.-_")=="?:!.-_"
    assert shorten(".")=="."

if __name__=="__main__":
    main() 
    
        