"""
Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.

"""

First_Name = input("Please enter your first name: ")
Last_name = input("Please enter your last name: ")

Name = First_Name + " " + Last_name

print(f"Hello, {Name}! Welcome to the Python Program.")

