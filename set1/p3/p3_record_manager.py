# Full Name: Jhasmine M. Aquino
# Section: IV-BSIT-A
# Activity Code: P3: Student Record Manager 
# Date: November 22, 2026

# Lists for storing student names
students = []
# Set for storing lowercase names para macheck if may duplicates
namesLower = set()

def addStudent():
    name = input("Enter student name: ").strip()

# Checks if name is empty
    if name == "":
        print("Name is empty! Please enter student name.")
        return

# Checks if the student already exists, for ex. "Jhasmine" is same lang sa "jhasmine"
    if name.lower() in namesLower:
        print("Student already exists!")

# Adds the student entered, kapag wala pang kapareho
    else:
        students.append(name.title())
        namesLower.add(name.lower())
        print("================================")
        print("Student", name.title(), "was successfuly added.")

def removeStudent():
    name = input("Enter student name to remove: ").strip()

    if name.lower() in namesLower:

# Checks if nasa list ung name na ireremove
        for student in students:
            if student.lower() == name.lower():
                students.remove(student)

        namesLower.remove(name.lower())
        print("================================")
        print("Student", name.title(), "was successfuly removed.")

    else:
        print("Student not found.")

def searchStudent():
    word = input("Search student name: ").strip().lower()
    found = []

# Checks if the entered word matches any part of the names na narecord
    for student in students:
        if word in student.lower():
            found.append(student)

    if len(found) == 0:
        print("No student match found.")
    else:
        print("Search results: ")
        for student in found:
            print("-", student)

def displayStudents():
    if len(students) == 0:
        print("No students yet.")
        return

# Arranges the student name in alphabetical order
    students.sort()
    print("\n===== List of Students =====")

# Every start ng name may number starting sa 1
    count = 1
    for student in students:
        print(str(count) + ".", student)
        count += 1
    print("\nTotal students: ", len(students))


def main():
    # This makes the menu to keep showing hanggang mag exit
    while True:
        print("\n=== Student Record Manager ===")
        print("1. Add student")
        print("2. Remove student")
        print("3. Search student")
        print("4. Display all students")
        print("5. Exit")
        print("================================")

        choice = input("What would you like to do? [1-5]: ")
        print("================================")

        if choice == "1":
            addStudent()
        elif choice == "2":
            removeStudent()
        elif choice == "3":
            searchStudent()
        elif choice == "4":
            displayStudents()
        elif choice == "5":
            print("Thank you for using Student Record Manager.")
            break
        else:
            print("Invalid choice! Please try again.")

main()

# A list can store many items, allows duplicates, and keeps them in order.
# A set does not allow duplicate items and is useful for checking if a name already exists. 
# In my program, I used a list (students) to store and sort student names so I can display them with numbers. 
# I also used a set (namesLower) to check for duplicate names, even if they have different uppercase and lowercase letters, like Jhasmine Aquino and jhasmine aquino.