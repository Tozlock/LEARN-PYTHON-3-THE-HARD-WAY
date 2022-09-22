# Asking Questions

print("How old are you?", end=' ')
age = input()

print("How tall are you?", end=' ')
height = float(input())

print("How much do you weigh?", end=' ')
weigh = float(input())

bmi = weigh / (height**2)
ponderal_index = weigh / (height**3)

print(
    f"So, you're {age} old, {height}m tall, and {weigh} kg heavy." +
    f"\nYour Body Mass Index(BMI) is: {bmi:.2f} kg/m\u00b2," +
    f"\nand your Ponderal Index(PI) is: {ponderal_index:.2f} kg/m\u00b3")
