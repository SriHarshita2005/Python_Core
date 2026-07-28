# • Write a Python program using a context manager (with) to open a text file in read mode,
# read the entire content using read(), and print the number of characters in the file.

with open(filename,"r") as file:
    content = file.read()
    print("Length of file:",len(content))

# Write a program that opens a file using a context manager, reads all lines using readlines(),
# and prints only the lines that contain more than 10 characters.

with open(filename , "r") as file:
    content = file.readlines()
    for i in content:
        if len(i.strip()) > 10:
            print(i.strip())

#  Write a program that creates a file and writes 3 lines using write(),
# reopens the same file in append mode, appends 2 more lines,
# and finally reads and prints the complete file content.

with open(filename,"w") as file:
    file.write("Line1\n")
    file.write("Line2\n")
    file.write("Line3\n")
with open(filename,"a") as file:
    file.write("Line4\n")
    file.write("Line5\n")
with open(filename,"r") as file:
    content = file.read()
    print(content)

# Write a program that opens a file in read mode, reads the first 10 characters,
# prints the current cursor position using tell(), moves the cursor back to the
# beginning using seek(0), and reads the full content again.

with open(filename,"r") as file:
    data = file.read(10)
    print(file.tell())
    file.seek(0)
    content = file.read()
    print(content)

# Create a custom context manager using a class that opens a file in write mode in the __enter__ method,
# writes a line to the file, closes the file in the __exit__ method, and properly prints or logs any exception information received in __exit__.

class FileManager:
    def __enter__(self):


#  Create a custom context manager using @contextmanager from the contextlib module that opens a file, yields the file object,
# and ensures the file is closed even if an exception occurs.


# Write a program using a context manager that opens a file in read mode, uses a loop to read the file in small chunks(
# for example, 5 characters at a time), prints the cursor position after each read using tell(), uses seek() to move to a specific position, and continues reading from there.