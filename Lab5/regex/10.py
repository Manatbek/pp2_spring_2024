import re


inp_str = input("Введите строку в стиле camel case: ")


snake_case_str = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', inp_str).lower()


print(f'Строка в стиле "snake case": {snake_case_str}')