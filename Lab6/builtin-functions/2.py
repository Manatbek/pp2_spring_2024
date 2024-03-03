def calcualte(word):
    Upp = 0
    low = 0
    for i in range(len(word)):
        if word[i] >= 'A' and word[i] <= 'Z':
            Upp += 1
        elif word[i] >= 'a' and word[i] <= 'z':
            low += 1
            
    print (Upp, low)


x = str(input(""))
calcualte(x)