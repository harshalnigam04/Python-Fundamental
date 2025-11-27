#        Problem Statement:  Write a Python program that:
#1. 	Takes an integer input from the user.
#2. 	Checks whether the number is even or odd using an if-else statement.
#3. 	Displays the result accordingly.





number=int(input("Enter a number :"))

if(number%2==0):
    print(f"{number} number is even")
else:
    print(f"{number} number is odd")
