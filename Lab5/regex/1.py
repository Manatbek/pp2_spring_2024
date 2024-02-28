import re


x = re.compile(r'a*b*')



y = input("Enter a string: ")


if x.fullmatch(y):
    print(f'The string "{y}" matches the pattern.')
else:
    print(f'The string "{y}" does not match the pattern.')