def main():
    greeting=input("insert bank greeting: ").strip().lower()
    print(f"${value(greeting)}")


def value(greeting):
    try:
        first_letters=greeting[0:5]
        if first_letters=="hello": # ALT: hello, 
            return(0)
        elif greeting[0]=="h":
            return(20)
        else:
            return(100)
    except IndexError:
        if greeting[0]=="h":
            return(20)
        else:
            return(100)


if __name__ == "__main__":
    main()