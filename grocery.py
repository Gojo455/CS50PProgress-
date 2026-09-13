items = {}
while True:
    try:
        item = input("Grocery: ")
        item = item.upper()
        if item == ""
        continue
        if item in items:
            items[item] += 1
        else:
            items[item] = 1
    except EOFError:
        break
for i in sorted(items):
    sort = items[i]
    print(f"{sort} {i} ")
