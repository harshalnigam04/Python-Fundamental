# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.


try:
    # Take user input
    user_input = input("Enter text to write to the file: ")

    # Write input to the file
    try:
        with open("output.txt", "w") as file:
            file.write(user_input + "\n")
    except IOError:
        print("Error: An I/O error occurred while writing to the file.")

    # Take additional input
    additional_input = input("Enter additional text to append: ")

    # Append input to the file
    try:
        with open("output.txt", "a") as file:
            file.write(additional_input + "\n")
    except IOError:
        print("Error: An I/O error occurred while appending to the file.")

    # Read and display final content
    try:
        print("\nFinal content of output.txt:")
        with open("output.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: An I/O error occurred while reading the file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
