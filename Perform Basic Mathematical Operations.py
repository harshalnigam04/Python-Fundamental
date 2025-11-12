"""
Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.

"""

num1 = float(input("Please enter a number: "))
num2 = float(input("Please enter another number: "))

Addition = num1 + num2
Subtraction = num1 - num2
Multiplication = num1 * num2
Division = num1 / num2

print(f"Addition: {Addition}")
print(f"Subtraction: {Subtraction}")
print(f"Multiplication: {Multiplication}")
print(f"Division: {Division}")