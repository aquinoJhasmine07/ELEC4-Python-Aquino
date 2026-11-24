# Full Name: Jhasmine M. Aquino
# Section: IV-BSIT-A
# Activity Code: P2: Custom Module: student_utils
# Date: November 22, 2026


# Imports the student_utils module and the functions needed for the program
import student_utils
from student_utils import computeAverage, determineStatus
from datetime import datetime

# Function for entering grades and checking if the entered grade is valid.
def enterGrades ():
    grades = []

    # Asks how many grades the student wants to enter.
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
                print("Invalid input! Please enter a number.")

    return grades

# Displays the student grade report
def main():

    print("====== STUDENT GRADE REPORT =====")

    grades = enterGrades()

# Gets the average and grade status using the from import style
    averageGrade = computeAverage(grades)
    status = determineStatus(grades)

# Gets the highest and lowest grade using the import module style
    highest = student_utils.highestGrade(grades)
    lowest = student_utils.lowestGrade(grades)

# Gets the current date and time 
    reportDate = datetime.now()

    print("========== GRADE RESULTS ==========")
    print("Grades: ", grades)
    print(f"Average: {averageGrade:.2f}")
    print(f"Highest Grade: {highest}")
    print(f"Lowest Grade: {lowest}")
    print(f"Status: {status}")
    print("Report Generated: ", reportDate.strftime("%B %d, %Y %I:%M %p")) 

# Checks if the file is run directly before starting the program.
if __name__ == "__main__":
    main()