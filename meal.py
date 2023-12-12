def main():
    time=convert(input("what time is it?"))
    if 7<=time<=8:
        print("breakfast time")
    elif 12<=time<=13:
        print("lunch time")
    elif 18<=time<=19:
        print("dinner time")
        

# convert time: 7:30 -> 7.5
def convert(time):
    hours=int(time.split(":")[0])
    minutes=int(time.split(":")[1])/60
    return hours+minutes


if __name__ == "__main__":
    main()