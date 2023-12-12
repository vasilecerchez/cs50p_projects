






import random

def main():
    level=get_level()
    score=0
    for _ in range(10):
        x,y=generate_integer(level)
        tre_prove=True
        for _ in range(3):
            result=int(input(f"{x} + {y} = "))
            if result==(x+y):
                score+=1
                tre_prove=False
                break
            else:
                print("EEE")
        if tre_prove==True:
            print(f"{x} + {y} = {x+y}")
    print(f"Score: {score}")



def get_level():
    level=input("Level: ")
    if level in ["1","2","3"]:
        return level
    else:
        return get_level() # without return-> error

def generate_integer(level):
    if level=="1":
        x, y=[random.choice(range(0,10)), random.choice(range(0,10))]
    elif level=="2":
        x, y=[random.choice(range(10,100)), random.choice(range(10,100))]
    elif level=="3":
        x, y=[random.choice(range(100,1000)), random.choice(range(100,1000))]

    return x, y


if __name__ == "__main__":
    main()
