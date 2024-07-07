import os

def list_directory_contents(path):
    try:
        #  this will list all files and directories in the given path
        contents = os.listdir(path)
        
        # this will print the items in the directory
        for item in contents:
            print(item)
    
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    
    except PermissionError:
        print(f"Error: Permission denied for directory '{path}'.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# this will prompt the user for a dirctory
directory_path = input("Enter the directory: ")

list_directory_contents(directory_path)
