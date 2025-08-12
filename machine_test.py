def add_student(students, name, marks):
    if name in students:
        print("Student already exists.")
    else:
        students[name] = marks
        print("Student added successfully!")


def calculate_average(marks):
    return round(sum(marks) / len(marks), 2)


def display_students(students):
    if not students:
        print("No students found.")
        return
    for name, marks in students.items():
        avg = calculate_average(marks)
        print(f"Name: {name} | Marks: {marks} | Average: {avg}")


def find_topper(students):
    if not students:
        print("No students found.")
        return
    topper_name = None
    topper_avg = 0
    for name, marks in students.items():
        avg = calculate_average(marks)
        if avg > topper_avg:
            topper_avg = avg
            topper_name = name
    print(f"Topper: {topper_name} (Average: {topper_avg})")


def main():
    students = {}
    while True:
        print("\n--- Student Marks Analysis ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Find Topper")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            marks_input = input("Enter marks (comma separated): ")
            try:
                marks = [int(x) for x in marks_input.split(",")]
                add_student(students, name, marks)
            except ValueError:
                print("Invalid marks. Please enter numbers separated by commas.")
        
        elif choice == "2":
            display_students(students)
        
        elif choice == "3":
            find_topper(students)
        
        elif choice == "4":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
