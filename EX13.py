# Parameters, Unpacking, Variables

from sys import argv

# read the What You Should See(WYSS) section for how to run this
# script, first, second, third = argv

# print(f"The Script is called: {script}")
# print("Your First variable is: ", first)
# print("Your Second variable is: ", second)
# print("Your Third variable is: ", third)

script, first = argv
print(f"The Script is called: {script}")

print("Your First Name is: ", first.capitalize())

lastName = input("What is your Last Name? ")

print(f"So, your full name is: {first.capitalize()} {lastName.capitalize()}")
