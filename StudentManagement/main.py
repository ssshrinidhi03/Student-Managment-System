student = []


def calculate_grade(average_marks):
    if average_marks >= 90:
        return "A"
    elif average_marks >= 80:
        return "B"
    elif average_marks >= 70:
        return "C"
    elif average_marks >= 60:
        return "D"
    else:
        return "F"


def add_student():
    name = input("Enter student name: ")
    roll = int(input("Enter student roll number: "))

    maths = float(input("Enter marks in Maths: "))
    if not (0 <= maths <= 100):
        print("Invalid marks for Maths. Please enter a value between 0 and 100.")
        return
    physics = float(input("Enter marks in Physics: "))
    if not (0 <= physics <= 100):
        print("Invalid marks for Physics. Please enter a value between 0 and 100.")
        return
    chemistry = float(input("Enter marks in Chemistry: "))
    if not (0 <= chemistry <= 100):
        print("Invalid marks for Chemistry. Please enter a value between 0 and 100.")
        return
    english = float(input("Enter marks in English: "))
    if not (0 <= english <= 100):
        print("Invalid marks for English. Please enter a value between 0 and 100.")
        return
    computer_science = float(input("Enter marks in Computer Science: "))
    if not (0 <= computer_science <= 100):
        print(
            "Invalid marks for Computer Science. Please enter a value between 0 and 100."
        )
        return

    total_marks = maths + physics + chemistry + english + computer_science
    average_marks = total_marks / 5
    grade = calculate_grade(average_marks)

    student.append(
        {
            "name": name,
            "roll": roll,
            "maths": maths,
            "physics": physics,
            "chemistry": chemistry,
            "english": english,
            "computer_science": computer_science,
            "average_marks": average_marks,
            "grade": grade,
        }
    )
    print(f"Student {name} added successfully.")


def display_students():
    if not student:
        print("No students found.")
        return

    for s in student:
        print(
            f"Name: {s['name']}, Roll: {s['roll']}, Average Marks: {s['average_marks']:.2f}, Grade: {s['grade']}"
        )


def update_student():
    roll = input("Enter student roll number to update: ")
    for s in student:
        if s["roll"] == roll:
            print(f"Updating student {s['name']} (Roll: {s['roll']})")
            s["maths"] = float(input("Enter new marks in Maths: "))
            s["physics"] = float(input("Enter new marks in Physics: "))
            s["chemistry"] = float(input("Enter new marks in Chemistry: "))
            s["english"] = float(input("Enter new marks in English: "))
            s["computer_science"] = float(
                input("Enter new marks in Computer Science: ")
            )

            total_marks = (
                s["maths"]
                + s["physics"]
                + s["chemistry"]
                + s["english"]
                + s["computer_science"]
            )
            average_marks = total_marks / 5
            grade = calculate_grade(average_marks)

            s["average_marks"] = average_marks
            s["grade"] = grade

            print(f"Student {s['name']} updated successfully.")
            return
    print(f"No student found with roll number {roll}.")


def search_student():
    roll = input("Enter student roll number to search: ")
    for s in student:
        if s["roll"] == roll:
            print(
                f"Name: {s['name']}, Roll: {s['roll']}, Average Marks: {s['average_marks']:.2f}, Grade: {s['grade']}"
            )
            return
    print(f"No student found with roll number {roll}.")


def view_marksheet():
    roll = input("Enter student roll number to view marksheet: ")
    for s in student:
        if s["roll"] == roll:
            print(f"Marksheet for {s['name']} (Roll: {s['roll']}):")
            print(f"Maths: {s['maths']}")
            print(f"Physics: {s['physics']}")
            print(f"Chemistry: {s['chemistry']}")
            print(f"English: {s['english']}")
            print(f"Computer Science: {s['computer_science']}")
            print(f"Average Marks: {s['average_marks']:.2f}")
            print(f"Grade: {s['grade']}")
            return
    print(f"No student found with roll number {roll}.")


def delete_student():
    roll = input("Enter student roll number to delete: ")
    for s in student:
        if s["roll"] == roll:
            student.remove(s)
            print(f"Student {s['name']} (Roll: {s['roll']}) deleted successfully.")
            return
    print(f"No student found with roll number {roll}.")


while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Student")
    print("4. Search Student")
    print("5. View Marksheet")
    print("6. Delete Student")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        search_student()
    elif choice == "5":
        view_marksheet()
    elif choice == "6":
        delete_student()
    elif choice == "7":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
