students = []

def add_student():
    print("\n----- Add Student -----")
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = {
        "Roll": roll,
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks
    }

    students.append(student)
    print("Student Added Successfully!\n")


def view_students():
    print("\n----- Student Records -----")

    if len(students) == 0:
        print("No student records found.\n")
        return

    for s in students:
        print("-" * 40)
        print("Roll   :", s["Roll"])
        print("Name   :", s["Name"])
        print("Age    :", s["Age"])
        print("Course :", s["Course"])
        print("Marks  :", s["Marks"])
    print("-" * 40)


def search_student():
    roll = input("\nEnter Roll Number to Search: ")

    for s in students:
        if s["Roll"] == roll:
            print("\nStudent Found")
            print("Roll   :", s["Roll"])
            print("Name   :", s["Name"])
            print("Age    :", s["Age"])
            print("Course :", s["Course"])
            print("Marks  :", s["Marks"])
            return

    print("Student Not Found!")


def update_student():
    roll = input("\nEnter Roll Number to Update: ")

    for s in students:
        if s["Roll"] == roll:
            print("Student Found")
            s["Name"] = input("Enter New Name: ")
            s["Age"] = int(input("Enter New Age: "))
            s["Course"] = input("Enter New Course: ")
            s["Marks"] = float(input("Enter New Marks: "))
            print("Record Updated Successfully!")
            return

    print("Student Not Found!")


def delete_student():
    roll = input("\nEnter Roll Number to Delete: ")

    for s in students:
        if s["Roll"] == roll:
            students.remove(s)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")


def highest_marks():
    if len(students) == 0:
        print("No Records Found!")
        return

    top = students[0]

    for s in students:
        if s["Marks"] > top["Marks"]:
            top = s

    print("\nHighest Scorer")
    print("Roll   :", top["Roll"])
    print("Name   :", top["Name"])
    print("Marks  :", top["Marks"])


def average_marks():
    if len(students) == 0:
        print("No Records Found!")
        return

    total = 0

    for s in students:
        total += s["Marks"]

    avg = total / len(students)

    print("\nAverage Marks =", round(avg, 2))


while True:

    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Highest Marks")
    print("7. Average Marks")
    print("8. Exit")

    choice = input("Enter Your Choice: ")

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
        highest_marks()

    elif choice == "7":
        average_marks()

    elif choice == "8":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")