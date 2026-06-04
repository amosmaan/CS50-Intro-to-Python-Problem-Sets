from pyfiglet import Figlet
import random 
import sys 
figlet = Figlet()

if len(sys.argv) == 1:
    x = random.choice(figlet.getFonts())
    figlet.setFont(f=x)
    text = input("Input: ")
    print (figlet.renderText(text))
elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font") and sys.argv[2] in figlet.getFonts():
    figlet.setFont(f = sys.argv[2])
    text = input("Input:")
    print (figlet.renderText(text))
else:
    sys.exit("invalid usage")


    


