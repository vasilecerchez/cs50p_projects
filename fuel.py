
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
    
