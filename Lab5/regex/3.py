import re

x = re.compile(r'[a-z]+_[a-z]+')

y = input("Enter a string: ")

matches = x.findall(y)
print(f'Sequences of lowercase letters joined with an underscore: {matches}')