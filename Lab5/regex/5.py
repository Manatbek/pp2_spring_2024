import re

x = re.compile(r'a.*b$')

h = input("Enter a string: ")

if x.match(h):
    print(f'The string "{h}" matches the pattern.')
else:
    print(f'The string "{h}" does not match the pattern.')