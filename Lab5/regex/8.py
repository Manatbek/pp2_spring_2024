import re

x = input("Enter a string: ")
res_list = re.findall('[A-Z][^A-Z]*', x)
print(f'The split string at uppercase letters: {res_list}')