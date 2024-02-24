x = int(input("print number: "))
for i in range(x):
    if i % 2 == 0:
        if (x - 2) == i or (x - 1) == i:
            print(i)
            break
        print(i, end = ", ")