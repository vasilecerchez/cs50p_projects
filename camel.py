# Solution 1 (no hint)
"""
name_camel=input("camelCase: ")
name_snake=""
for l in name_camel:
    if l.isupper()==False:
        name_snake=name_snake+l
    else:
        name_snake=name_snake+"_"+l.lower()

print(f"snake_case: {name_snake}")

"""


#Solution 2 (hint)

name_camel=input("camelCase: ").strip()
print("snake_case: ", end="")

## "This is for when the first letter is uppercase.
#if name_camel[0].isupper()==True:
#    name_camel=name_camel[0].lower()+name_camel[1:]
    
for l in name_camel:
    if l.isupper()==False:
        print(l,end="")
    else:
        print("_"+l.lower(),end="")

        
    