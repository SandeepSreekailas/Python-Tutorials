# Student Marks Analysis
def add_student(students, name, marks):
    if name in students:
        print("Student already exists.")
    else:
        students[name] = marks
        print("Student added successfully!")

# Function to calculate average of a list of marks
def calculate_average(marks):
    if len(marks) == 0:
        return 0
    return round(sum(marks) / len(marks), 2)

# Function to display all students
def display_students(students):
    if not students:
        print("No students to display.")
    for name, marks in students.items():
        avg = calculate_average(marks)
        print(f"Name: {name} | Marks: {marks} | Average: {avg}")

# Function to find the topper(s)
def find_topper(students):
    if not students:
        print("No students to analyze.")
        return
    max_avg = -1
    toppers = []
    for name, marks in students.items():
        avg = calculate_average(marks)
        if avg > max_avg:
            max_avg = avg
            toppers = [name]
        elif avg == max_avg:
            toppers.append(name)
    print("Topper(s):")
    for topper in toppers:
        print(f"{topper} (Average: {max_avg})")

# Main program loop
def main():
    students = {}
    while True:
        print("\n--- Student Marks Analysis ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Find Topper")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter student name: ").strip()
            marks_input = input("Enter marks (comma separated, e.g., 85,90,78): ").strip()
            try:
                marks = [int(mark.strip()) for mark in marks_input.split(",")]
                add_student(students, name, marks)
            except ValueError:
                print("Invalid marks! Please enter integers separated by commas.")
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            find_topper(students)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


main()