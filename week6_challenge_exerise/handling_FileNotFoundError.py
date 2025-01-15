# Handling file not found error message that asks the user for a file name

def get_file_name():
    while True:
        try:
            file_name = input("Enter a file name to search if its on this directory: ") 
            with open(file_name) as f:
                print(f"File {file_name} found.")
                print(f.read())
                return
                      
        except FileNotFoundError:
            print("File not found. Please try again.")

get_file_name()