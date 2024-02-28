import re

x = input("Enter a string: ")
Res = re.sub(r'[ ,.]', ':', x)
print(f'The modified string is: {Res}')