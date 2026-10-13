
while True:
    try:
        fraction = input("Fraction: ")

        if "/" not in fraction:
            continue
        else:
            idx = fraction.index("/")
            x = fraction[:idx]
            y = fraction[idx +1:]
            if not (x.isdigit() and y.isdigit()):
                continue
            x,y = int(x), int(y)
            if (x and y ) < 0:
                continue
            if x > y or y == 0:
                continue
        fuel = round((x/y)*100)
        break
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
if fuel >= 99:
    print("F")
elif fuel <= 1:
    print("E")
else:
    print(f"{fuel}%")
