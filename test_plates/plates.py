


def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not 2<=len(s)<=6:
        return False
    elif s[0].isnumeric() or s[1].isnumeric():
        return False
    for i in range(len(s)):
        if punctuation(s[i]):
            return False
        elif (s[i]).isnumeric():
            if (s[i]).isnumeric() and s[i]!="0" and (s[i:]).isnumeric():
                return True
            return False
    return True
            
def punctuation(text):
    for i in [" ", ".",',',"!","?"]:
        if i in text:
            return True
    return False 

    
if __name__ == "__main__":
    main()