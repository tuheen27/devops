'''
Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
Add a new student and grade.
Update an existing student’s grade.
Print all student grades.

Used dictionary and basic operations. Using if else:

'''
students = {}
def add_student(name, grade):
    students[name] = grade
    print(f"Added {name} with grade {grade}.")
def update_student(name, grade):
    if name in students:
        students[name] = grade
        print(f"Updated {name}'s grade to {grade}.")
    else:
        print(f"{name} not found in the records.")
def print_grades():
    if students:
        print("Student Grades:")
        for name, grade in students.items():
            print(f"{name}: {grade}")
    else:
        print("No students found.")
while True:
    print("\nOptions:")
    print("1. Add student")
    print("2. Update student grade")
    print("3. Print all student grades")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter student's name: ")
        grade = input("Enter student's grade: ")
        add_student(name, grade)
    elif choice == '2':
        name = input("Enter student's name to update: ")
        grade = input("Enter new grade: ")
        update_student(name, grade)
    elif choice == '3':
        print_grades()
    elif choice == '4':
        break
    else:
        print("Invalid choice, please try again.")  
# This code allows users to manage a list of students and their grades using a dictionary.            