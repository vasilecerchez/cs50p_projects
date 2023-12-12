

gro_list={}

while True:
    try:
        item=input().strip().lower()
        #if item not in gro_list:
        #    gro_list[item]=1
        #else:
        #    gro_list[item]+=1
        gro_list[item]+=1
    except KeyError:
        gro_list[item]=1
        
    except EOFError:
        break
        
for i in sorted((gro_list.keys())):
    print(f"{gro_list[i]} {i.upper()}")
        
                    
            