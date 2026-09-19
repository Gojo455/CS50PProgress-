def main():
    ask = input("Time:")
    ask = convert(ask)
    if 7 <= ask < 8:
        print("breaskfast time")
    elif 12 < ask < 13:
        print("lunch time")
    elif 18 < ask < 19:
        print("dinner time")


def convert(time):
    for i,char in enumerate(time):
        if char in [":"]:
            hour = time[:i]
            minute = time[i + 1:]
            hour = float(hour)
            minute = float(minute)/60
    final = hour + minute 
    return final 



if __name__ == "__main__":
    main()



