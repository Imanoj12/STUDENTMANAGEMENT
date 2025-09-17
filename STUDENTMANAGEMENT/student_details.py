import os

FILE_NAME = "students.txt"

# Function to add a student
def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{age},{grade}\n")
    print("Student added successfully!\n")

# Function to view all students
def view_students():
    if not os.path.exists(FILE_NAME):
        print("No students found.\n")
        return
    with open(FILE_NAME, "r") as file:
        print("Student Records:")
        for line in file:
            name, age, grade = line.strip().split(",")
            print(f"Name: {name}, Age: {age}, Grade: {grade}")
    print()

# Function to search a student by name
def search_student():
    search_name = input("Enter student name to search: ")
    found = False
    if not os.path.exists(FILE_NAME):
        print("No students found.\n")
        return
    with open(FILE_NAME, "r") as file:
        for line in file:
            name, age, grade = line.strip().split(",")
            if name.lower() == search_name.lower():
                print(f"Found: Name: {name}, Age: {age}, Grade: {grade}\n")
                found = True
                break
    if not found:
        print("Student not found.\n")

# Function to update a student record
def update_student():
    update_name = input("Enter student name to update: ")
    updated = False
    if not os.path.exists(FILE_NAME):
        print("No students found.\n")
        return
    
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
    
    with open(FILE_NAME, "w") as file:
        for line in lines:
            name, age, grade = line.strip().split(",")
            if name.lower() == update_name.lower():
                new_name = input("Enter new name: ")
                new_age = input("Enter new age: ")
                new_grade = input("Enter new grade: ")
                file.write(f"{new_name},{new_age},{new_grade}\n")
                updated = True
            else:
                file.write(line)
    
    if updated:
        print("Student updated successfully!\n")
    else:
        print("Student not found.\n")

# Function to delete a student record
def delete_student():
    delete_name = input("Enter student name to delete: ")
    deleted = False
    if not os.path.exists(FILE_NAME):
        print("No students found.\n")
        return
    
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
    
    with open(FILE_NAME, "w") as file:
        for line in lines:
            name, age, grade = line.strip().split(",")
            if name.lower() != delete_name.lower():
                file.write(line)
            else:
                deleted = True
    
    if deleted:
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")

# Main menu
def menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.\n")

# Run the program
menu()
