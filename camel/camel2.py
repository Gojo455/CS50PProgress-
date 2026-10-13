camel = input("Camel: ")
snake = ""

upper = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
for words in camel:
    if words in upper:
        snake += "_" + words.lower()
    else:
        snake += words

print(snake)