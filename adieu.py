

"""
#  Adieu, adieu, to marc, anto(NO COMMA) and enzo
names=[]
while True:
    try:
        name=input("Name: ").strip()
        names.append(name)
    except EOFError:
        try:
            print("Adieu, adieu, to ", end="")
            for i in range(len(names)-2):
                print(f"{names[i]}, ",end="")
            print(f"{names[-2]} and {names[-1]}")
            break
        except IndexError:
            print("Adieu, adieu, to ", end="")
            print(f"{names[0]} and {names[1]}")
            
"""
"""
# solution2
#  Adieu, adieu, to marc, anto(COMMA) and enzo
# But no join
names=[]
while True:
    try:
        name=input("Name: ").strip()
        names.append(name)
    except EOFError:
        try:
            print("Adieu, adieu, to ", end="")
            for i in range(len(names)-1):
                print(f"{names[i]}, ",end="")
            print(f"and {names[-1]}")
            break
        except IndexError:
            print("Adieu, adieu, to ", end="")
            print(f"{names[0]} and {names[1]}")

"""
import inflect
names=[]
p=inflect.engine()
while True:
    try:
        name=input("Name: ").strip()
        names.append(name)
    except EOFError:
        # print
        break
    
names=p.join(names)
print()
print("Adieu, adieu, to ", end="")
print(names)
    


        