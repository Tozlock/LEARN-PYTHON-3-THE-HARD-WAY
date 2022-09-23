# More Files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.\n")
in_file = open(from_file, encoding="utf8")
in_data = in_file.read()

print(f"The input file is {len(in_data)} bytes long")

print(f"Does the output file exist? {exists(to_file)}.")
print("Ready, hit RETURN to contonue, CTRL - C TO abort.")
input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print("Alright, all done.")
out_file.close()
in_file.close()

# first make a sample file
# echo "This is a test file." > test.txt
# then look at it
# cat test.txt
# This is a test file.
