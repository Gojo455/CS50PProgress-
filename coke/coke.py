debt = 50 
due = 0
while debt > 0:
    amount = int(input("Insert coin: "))
    if amount in [25,10,5]:
        debt -= amount
        if debt > 0:
            print(f"Amount owed: {debt}")
change = debt * -1
print(f"Change owed: {change}")