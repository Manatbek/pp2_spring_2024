import os

def way(path):
    try:
        entries = os.listdir(path)

        for entry in entries:
            print(entry)

    except FileNotFoundError:
        print(f"Error: The specified path '{path}' does not exist.")

path_inp = input("Enter the path: ")
way(path_inp)