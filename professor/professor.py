import random
def main():
    lvl = get_level()
    score = 0
    for _ in range(10):
        x= generate_integer(lvl)
        y = generate_integer(lvl)
        correct = x + y
        # cook a correct function to track operators later
        for i in range(3):
            try:
                z = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE") 
            else:
                if correct == z:
                    score += 1
                    break
                else:
                    print("EEE")
            if i == 2:
                print(f"Correct answer: {correct}")
    print(f"Score: {score}")
def get_level(prompt="Level: "):
    while True:
        try:
            level = int(input(prompt))
        except ValueError:
            continue
        else:
            if level in [1,2,3]:
                return level
def generate_integer(level):
    if level not in [1,2,3]:
        raise ValueError
    if level == 1:
        low = 0
    else:
        low = 10 **(level -1)
    high = (10 ** level) - 1
    return(random.randint(low,high))
if __name__ == "__main__":
    main()