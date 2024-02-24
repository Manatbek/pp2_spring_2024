a = int(input("print number: "))
for n in range (a + 1):
    if n % 4 == 0 and n % 3 == 0:
        print(n, end = " ")