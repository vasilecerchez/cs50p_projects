


def main():
    tweet=input("Input: ").strip()
    print("Output: ", end="")
    print(shorten(tweet),end="")


def shorten(word):
    t=""
    for l in word:
        if l.lower() not in ["a","e","i","o","u"]:
            t=t+l
    return t

    

if __name__ == "__main__":
    main()