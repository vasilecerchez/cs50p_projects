






import random

while True:
    level=(input("Level: "))
    try:
        level=int(level)
        while level<=0:
            level=int(input("Level: "))
        secret_number=random.choice(range(1,level+1))
        break
    except ValueError:
        pass
    
while True:   
    users_number=input("Guess: ")      
    try:
        users_number=int(users_number)
        if users_number<0:
            pass
        elif users_number>secret_number:
            print("Too large!")
            pass
        elif users_number<secret_number:
            print("Too small!")
            pass
        else:
            print("Just right!")
            break
    except ValueError:
        pass


        
        
    

    
