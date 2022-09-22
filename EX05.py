# - - coding: utf- 8 - -
name = 'Shady Moustafa'
age = 37  # not a lie
height = 1.65  # meters
weight = 65  # Kilograms
eyes = 'Green'
teeth = 'white'
hair = 'Dark Brown'
kilo = 2.2
meters = 39.37

print("Let's talk about %s." % name)
print("He's %r inches tall." % (height * meters))
print(f"He's {height} meters tall.")
print("He's %d pounds heavy." % (weight * kilo))
print(f"He's {weight} Kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
