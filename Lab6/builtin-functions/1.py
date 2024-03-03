def multiply(numbers):
    x = 1
    for i in numbers:
        x *= int(i)
        
    print(x)


inp = input("print numbers: ")
arr = inp.split()
list = []
for i in range (len(arr)):
    list.append(arr[i])
    
multiply(list)