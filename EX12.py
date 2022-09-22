# Prompting People

age = int(input("How old are you? "))

height = float(input("How tall are you? "))

weigh = float(input("How much do you weigh ?"))

bmi = weigh / (height**2)
ponderal_index = weigh / (height**3)

print(
    f"So, you're {age} years old, {height}m tall, and {weigh} kg heavy." +
    f"\nYour Body Mass Index(BMI) is: {bmi:.2f} kg/m\u00b2," +
    f"\nand your Ponderal Index(PI) is: {ponderal_index:.2f} kg/m\u00b3")
