import math
a = int(input("Input number of sides: "))
b = int(input("Input the length of a side: "))
n = a * b ** 2
m = 4 * math.tan(math.pi / a)
area = n / m
print("The area of the polygon is:", area)