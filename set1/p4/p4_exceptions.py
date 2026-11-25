# Full Name: Jhasmine M. Aquino
# Section: IV-BSIT-A
# Activity Code: P4: Safe Menu Program 
# Date: November 23, 2026

def divideNumbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1/num2

    except ValueError: # Error if the user entered letters/symbols
        print("===================================")
        print("Error: Please enter numbers only.")

    except ZeroDivisionError: # Error if the user entered 0 for the second number
        print("===================================")
        print("Error: Cannot divide by zero.")

    else: 
        print("===================================")
        print(f"Result: {result}")

    finally: # Madidisplay palagi kahit na may error or wala
        print("\nDivision done.")

def openFile():
    filename = input("Enter file name: ")

    try:
        file = open(filename, "r")
        contents = file.read()
        file.close()
    except FileNotFoundError: # Error kapag hindi mahanap ang file
        print("===================================")
        print("Error: File not found.")
    else:
        print("\n===== File Contents =====")
        print(contents)
        print("===== End of File =====")
    finally: 
        print("\nFile operation done.")

def main():
    while True:
        print("\n===== Safe Menu Program =====")
        print("1. Divide two numbers")
        print("2. Open a file")
        print("3. Exit")
        print("===============================")

        choice = input("What would you like to do?[1-3]: ").strip()

        if choice == "1":
            divideNumbers()
        elif choice == "2":
            openFile()
        elif choice == "3":
            print("\nThank you for using Safe Menu Program.")
            break
        else:
            print("===================================")
            print("Invalid choice! Please choose from 1-3")

main()