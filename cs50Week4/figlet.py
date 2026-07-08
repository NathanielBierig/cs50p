from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
if len(sys.argv) not in [1, 3]:
    sys.exit("Invalid number of arguments")
    
elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid font argument")
    elif sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid font type")
    else:
        figlet.setFont(font = sys.argv[2])
else:
    figlet.setFont(font = random.choice(figlet.getFonts()))
  

s = input("Input: ")
print(figlet.renderText(s))

   
