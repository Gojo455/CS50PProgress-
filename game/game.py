import random
def main():
    level = checkvars("Level: ")
    ranint = random.randint(1,level)
# guess variable loop
    while True:
        guess = checkvars("Guess: ")
        if guess < ranint:      
            print("Too small!")
        elif guess > ranint:
            print("Too large!")
        else:
            print("Just right!")
            break
# function to validate both user inputs
def checkvars(no):
    while True:
        try:
            number = int(input(no))
        except ValueError:
            pass
        else:
            if number > 0:
                return number
            
main()