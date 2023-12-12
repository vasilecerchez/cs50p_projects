
# Solution 1
#answer=input("What is the Answer of the Great Question of Life, the Universe and Everything?").strip().lower()
#
#if answer=="42" or answer.lower()=="forty-two" or answer.lower()=="forty two":
#    print("Yes")
#else:
#    print("No")

#Solution 2
# lower does not return an error on a string of numbers
answer=input("What is the Answer of the Great Question of Life, the Universe and Everything? ").strip().lower()

if answer=="42" or answer=="forty-two" or answer=="forty two":
    print("Yes")
else:
    print("No")
    
    
"""
the solution above solves the problems of case sensitivity and spaces sensitivity
at the beginning and at the end of the string. But not the spaces between 
the words :  "forty     two"  or "4   2"

a solution could be to divide based on space and then group with split
and join (or a for loop with a list)

a="ciao   Milano"
a=" ".join(a.split())
print(a)

"""

