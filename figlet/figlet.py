import sys
import random
from pyfiglet import Figlet
figlet = Figlet()
# check 
if len(sys.argv) == 3:
    # if sys argument is either of -f or --font
    if sys.argv[1] in ["-f","--font"]:
        fnts = figlet.getFonts()
        # check if sys argument is in the retruned list of fonts
        if sys.argv[2] in fnts:
            figlet.setFont(font= sys.argv[2])
            print(figlet.renderText(input("Text: ")))
        else:
            sys.exit("Font not found")
    else:
        sys.exit(" Parameters not accurate")
elif len(sys.argv) == 1:
    gtfont = random.choice(figlet.getFonts())
    figlet.setFont(font=gtfont)
    txt = input("Text: ")
    print(figlet.renderText(txt))
else:
    sys.exit("Invalid parameters.")
    






