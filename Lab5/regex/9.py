import re

inp_str = input("Enter a string: ")
res_str = re.sub(r'(?<=[a-z])([A-Z])', r' \1', inp_str)
print(f'The modified string is: {res_str}')