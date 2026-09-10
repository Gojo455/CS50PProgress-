entry = input("Answer to the Great question: ")
entry = entry.lower()

if entry in ("42", "forty-two", "forty two"):
    print("Yes")
else:
    print("No")