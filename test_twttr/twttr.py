def main():
    tweet = input("Tweet: ")
    print(shorten(tweet))

# funcion to strip away vowels 
def shorten(word):
    final= ""
    for char in word:
        if char.upper() not in "AEIOU":
            final += char
    return final

if __name__ == "__main__":
    main()
