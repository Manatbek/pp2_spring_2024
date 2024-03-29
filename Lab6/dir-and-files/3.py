import os

def check(path):
    try:
        
        if os.path.exists(path):
            print(f"The path '{path}' exists.")

            
            fileterm = os.path.basename(path)
            directory = os.path.dirname(path)

            print(f"Filename: {fileterm}")
            print(f"Directory: {directory}")

        else:
            print(f"The path '{path}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

path_inp = input("Enter the path: ")
check(path_inp)