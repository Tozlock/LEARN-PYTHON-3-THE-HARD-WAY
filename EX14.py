# Prompting and Passing

from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd lide to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where Do you live?")
lives = input(prompt)

print("What kind of computers do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer, NicE.
""")
