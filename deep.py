"""
In deep.py, implement a program that 
prompts the user for the answer to the
Great Question of Life, the Universe 
and Everything, outputting Yes if the user 
inputs 42 or (case-insensitively) forty-two
or forty two. Otherwise output No."""
# ask user for input, then lower it so it matches the conditions
entry = input("Answer to the Great question: ")
entry = entry.lower()

if entry in ("42", "forty-two", "forty two"):
# the in key word only accepts strings on the left side
    print("Yes")
else:
    print("No")