import EX25 as ex25
# from EX25 import *

sentence = "hello, all good things come to those who wait."
words = ex25.break_words(sentence)

print("The sentence's words:")
print(words)
print()

sorted_words = ex25.sort_words(words)
print("The sorted words:")
print(sorted_words)
print()

print("The first word:")
ex25.print_first_word(words)
print()

print("The last word:")
ex25.print_last_word(words)
print()

print("The words without the first and last words:")
print(words)
print()

print("The first sorted word:")
ex25.print_first_word(sorted_words)
print()

print("The last sorted word:")
ex25.print_last_word(sorted_words)
print()

print("The sorted words without the first and last words:")
print(sorted_words)
print()

print("The sorted sentence:")
sorted_words = ex25.sort_sentence(sentence)
print(sorted_words)
print()

print("The first and last words:")
ex25.print_first_last(sentence)
print()

print("The first and last sorted words:")
ex25.print_first_last_sorted(sentence)
print()
print(help(ex25))
print()
print(help(ex25.break_words))
