# to open a file
#file_obj=open(file_name,acess_mode)

file = open("sample.txt", "w")
file.write("hello, this is a sample file.")
file.close()

# to read a file
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

# to append to a file
with open("sample.txt", "a") as file:
    file.write("\nThis is an appended line.")


# to handle files we can use with clause: which automatically closes the file

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)


#reading large files line by line- removes extra spaces and newlines

with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())

