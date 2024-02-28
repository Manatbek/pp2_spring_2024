import re

a = re.compile(r'ab{2,3}')

b = input("Enter a string: ")

if a.search(b):
    print(f'The string "{b}" matches the pattern.')
else:
    print(f'The string "{b}" does not match the pattern.')