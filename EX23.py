# Strings, Bytes, and Character Encodings

# 1. How modern computers store human languages for display and processing
# and how Python3 calls this strings
# 2. How you must “encode” and “decode” Python’s strings into a type called bytes
# 3. How to handle errors in your string and byte handling
# 4. How to read code and find out what it means even if you’ve never seen it before

import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<=====>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

raw_bytes = b'\xd8\xa7\xd9\x84\xd8\xb9\xd8\xb1\xd8\xa8\xd9\x8a'
utf_string = "العربية"

print(raw_bytes.decode())
print(utf_string.encode())

print(raw_bytes.decode() == utf_string)
print(utf_string.encode() == raw_bytes)
