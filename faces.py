def main():
    mssg = input("Message: ")
    mssged = convert(mssg)
    print(mssged)


def convert(x):
    if ":)" in x:
        x = x.replace(":)","🙂")
    if ":(" in x:
        x = x.replace(":(","🙁 ")
    return x

    
main()
