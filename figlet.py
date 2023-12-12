





from pyfiglet import Figlet
import sys
import random
figlet = Figlet()

try:
    if sys.argv[1] in ["-f","--font"]:
        f=sys.argv[2]
        figlet.setFont(font=f)
    else:
        sys.exit("Invalid usage")
        
except IndexError:
    f=random.choice(figlet.getFonts())
    figlet.setFont(font=f)
except EOFError:
    sys.exit("Invalid usage")
except:
    sys.exit("Invalid usage")

text=input("Input: ")

print(f"Output:\n{figlet.renderText(text)}")    
    
