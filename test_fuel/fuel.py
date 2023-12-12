"""
fraction=input("Fraction: ").strip()
try:
    num=int(fraction.split("/")[0])
    denom=int(fraction.split("/")[1])
    perc=round((num/denom)*100,0)
    if perc>100:
        fraction=input("Fraction: ").strip()
    elif perc<=1:
        print("E")
    elif perc>=99:
        print("F")
    else:
        print(f"{round((num/denom)*100)}%")
        
except (ValueError, ZeroDivisionError):
    fraction=input("Fraction: ").strip()
"""
"""
def main():
    fraction=input("Fraction: ").strip()
    print(gauge(convert(fraction)))
    


def convert(fraction):
    while True:
        try:
            num=int(fraction.split("/")[0])
            denom=int(fraction.split("/")[1])

            if num<denom:
                return (round((num/denom)*100))
            else:
                fraction=input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise 

def gauge(percentage):
    if percentage<=1: 
        return "E"
    elif percentage>99:
        return "F"
    else:
        return (f"{percentage}%")
        
if __name__ == "__main__":
    main()

"""


def main():
    fraction=input("Fraction: ").strip()
    print(gauge(convert(fraction)))
    
def convert(fraction):
    num,denom=fraction.split("/")
    if num.isdigit() is False or denom.isdigit() is False:
        raise ValueError
    elif int(denom)==0:
        raise ZeroDivisionError
    elif int(num)>int(denom):
        raise ValueError
    else:
        return round((int(num)/int(denom))*100)

def gauge(percentage):
    if percentage<=1: 
        return "E"
    elif percentage>99:
        return "F"
    else:
        return (f"{percentage}%")

if __name__ == "__main__":
    main()





