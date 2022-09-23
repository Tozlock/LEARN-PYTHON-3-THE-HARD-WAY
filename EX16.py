# Reading and Writing Files

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.\n")
print("If you don't want that, hit CTRL+c(^C).")
print("If you want that, hit Return")

input("?")
print("Opening the file...")
target = open(filename, 'w', encoding="utf8")

# The truncate() method resizes the file to the given number of bytes.
# If the size is not specified, the current position will be used.
# file.truncate(size)
# size is Optional. The size of the file (in bytes) after the truncate.
# Default None, which means the current file stream position.

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

target.write(f"{line1}\n{line2}\n{line3}\n")

print("And funally, we close it.")
target.close()
