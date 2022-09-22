# Reading Files

from sys import argv

script, filename = argv

txt = open(filename, encoding="utf8")

print(f"Here's your file {filename}:\n")
print(txt.read())
txt.close()

print("Type the filename again:")
file_agian = input("> ")

txt_again = open(file_agian, encoding="utf8")
print("\n" + txt_again.read())
txt_again.close()
