# Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.


students_marks = {
    "Alice": 85,
    "John": 78,
    "Charlie": 92,
    "Bob": 88
}
name = input("Enter the student's name: ")

if name in students_marks:
    print(f"{name}'s marks: {students_marks[name]}")
else:
    print("Student not found")
