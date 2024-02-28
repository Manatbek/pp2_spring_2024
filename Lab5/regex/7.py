import re
x = input("Enter a snake case string: ")
words = x.split('_')
camel_case_cord = words[0] + ''.join(word.capitalize() for word in words[1:])
print(f'The camel case string is: {camel_case_cord}')