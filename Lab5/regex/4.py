import re

x = re.compile(r'[A-Z][a-z]+')

y = input("Enter a string: ")

matches = x.findall(y)
print(f'Sequences of one uppercase letter followed by lowercase letters: {matches}')