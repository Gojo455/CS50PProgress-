while True:
    try:
        fraction = input("Fraction: ")
        fraction = fraction.replace(" ", "")
        x,y = fraction.split("/")
        if not (x.isdigit() and y.isdigit()):
            continue
        x = int(x)
        y = int(y)
        if x > y:
            continue
        if y == 0:
            continue
        fuel = round((x/y)*100)
        break
    except ValueError:
        continue
    # although dead code below cause y will never be equal to 0 
    except ZeroDivisionError:
        continue
if fuel >= 99:
    print("F")
elif fuel <= 1:
    print("E")
else:
    print(f"{fuel}%")

