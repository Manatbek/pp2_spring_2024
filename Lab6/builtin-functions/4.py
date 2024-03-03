import time
import math

def root(numbers, milliseconds):
    time.sleep(milliseconds / 1000.0)  
    result = math.sqrt(numbers)
    print(f"Square root of {numbers} after {milliseconds} milliseconds is {result}")


numbers = int(input("Enter the number: "))
milliseconds = int(input("Enter the delay in milliseconds: "))


root(numbers, milliseconds)