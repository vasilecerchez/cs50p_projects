# Soluzione 1 ................................................................
#greeting=input("insert bank greeting: ").strip().lower()
#first_world=greeting.split()[0]
#
#if first_world=="hello": # ALT: hello, 
#    print("$0")
#elif first_world[0]=="h":
#    print("$20")
#else:
#    print("$100")

"""
ALT, problems with: "hello," or "hello." "hello!" "hello,Newman"
"""

# Solution 3........................................................
# a="milano"
# b=[2:1000] -> lano
greeting=input("insert bank greeting: ").strip().lower()
first_letters=greeting[0:5]
if first_letters=="hello": # ALT: hello, 
    print("$0")
elif first_letters[0]=="h":
    print("$20")
else:
    print("$100")
    
# we can also use: if greeting.startswith("hello")


## Solution 2 ........................................................
#greeting=input("insert bank greeting: ").strip().lower()
## hello =  length 5  letters
#if len(greeting)>=5:# cases: "hello", "hello, jhon"
#    first_letters=greeting[0:5]
#    if first_letters=="hello": # ALT: hello, 
#        print("$0")
#    elif first_letters[0]=="h":
#        print("$20")
#    else:
#        print("$100")
#else: # casee when len(greeting)<5:
#    first_let=greeting[0]
#    if first_let=="h":
#        print("$20")
#    else:
#        print("$100")



