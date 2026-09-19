camel = input("Text: ")
check = ""
for char in camel:
    if char.isupper():
        check += "_" + char.lower()
    else:
        check += char.lower()
print(check)