#  Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results.



import math

num = float(input("Enter a number: "))

square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)

print("Square root:", square_root)
print("Logarithm:", natural_log)
print("Sine:", sine_value)
