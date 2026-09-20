expr = input("Expression: ")
for i, char in enumerate(expr):
    # enumerate returns the character and it's index 
    if char in ["+","-","*","/"]:
        operator = char
        x = expr[:i]
        y = expr[i+1:]
        x, y = x.replace(" ",""), y.replace(" ","")
        x,y = int(x), int(y)

if operator == "+":
    final = x + y
elif operator == "-":
    final = x - y
elif operator == "/":
    final = x / y
elif operator == "*":
    final = x * y
print(float(final))




