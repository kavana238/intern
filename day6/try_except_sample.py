try:
    file = open("missing_file.txt", "r")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print("The file was not found. Please check the file name and try again.")

except PermissionError:
    print("You do not have permission to access this file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")



#Exception is the base class for almost all built-in errors in Python
#ValueError
#TypeError
#IndexError
#ZeroDivisionError 
#e is a variable
#It stores the actual error message