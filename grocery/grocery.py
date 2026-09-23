grocery = {}
while True:
    try:
        item = input()
        item = item.upper()
        if item == "":
            continue 
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    except EOFError:
        break

for li in sorted(grocery):
    print(grocery[li], li)