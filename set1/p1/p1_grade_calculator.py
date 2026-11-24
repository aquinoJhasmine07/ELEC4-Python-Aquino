# Full Name: Jhasmine M. Aquino
# Section: IV-BSIT-A
# Activity Code: P1: Student Grade Calculator 
# Date: November 22, 2026

# Function for entering grades and checking if the entered grade is valid.
def enterGrades ():
    grades = []

# This asks how many grades the student wants to enter.
    while True:
        try:
            numberOfGrades = int(input("Number of grades to enter: "))

            if numberOfGrades > 0:
                break
            else:
                print("Please enter at least 1 grade.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")

# Ask the student to enter grade repeatedly until mareach ung number of grades na ininput
    for i in range(numberOfGrades):
        while True:
            try: 
                grade = float(input(f"Enter grade no. {i + 1}: "))

                if 0<= grade <=100: # Checks if the entered grade is from 0-100
                    grades.append(grade)
                    break

                else: 
                    print("Invalid grade! Please enter a number from 0 to 100.")

            except ValueError:
                print("Invalide input! Please enter a number.")

    return grades

# Adds all grades and divides them to the number of grades entered
def averageComputation(grades):
    return sum(grades)/len(grades)

# Get the highest grade
def highestGrade(grades):
    return max(grades)

# Get the Lowest grade
def lowestGrade(grades):
    return min(grades)

# Determining if the student passed or failed
def gradeStatus(grades):
    average = averageComputation(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"
    
def Results(grades):
    if len(grades) == 0: # Checks if mayroong grade na naenter
        print("Please enter grades first. No grades available.")
        return           

    average = averageComputation(grades)
    highest = highestGrade(grades)
    lowest = lowestGrade(grades)
    status = gradeStatus(grades)

    print("========== GRADE RESULTS ==========")
    print("Grades: ", grades)
    print(f"Average: {average:.2f}")
    print(f"Highest Grade: {highest}")
    print(f"Lowest Grade: {lowest}")
    print(f"Status: {status}")

studentGrades = []

# Keeps showing the menu until the student choose to exit
while True:

    print("========== STUDENT GRADE CALCULATOR ==========")
    print("[1] Enter Grades")
    print("[2] View Results")
    print("[3] Exit")
    print("==============================================")

    option = input("Choose from the options (1-3): ")


    if option == "1":
        studentGrades = enterGrades()
        print("==============================================")
        print("Grades successfully saved!")


    elif option == "2":
        Results(studentGrades)

    elif option == "3":
        print("Thank you for using the Grade Calculator!")
        break

    else:
        print("Invalid choice! Please select from 1-3.")
   