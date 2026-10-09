import inflect
# read doc for if module requres engine or functions can be used directly
p = inflect.engine()
final = []
while True:
    try:
        name = input("Name: ")
        final.append(name)
    except EOFError:
        
        print("Adieu, adieu, to " + p.join(final))
        break
