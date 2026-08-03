students = {
    "Ahmad" : {
        "age": 19,
        "marks": 88
    },
    "Ali" : {
        "age": 22,
        "marks": 93
    },
    "Arslan": {
        "age": 21,
        "marks": 90
    }
}

choice = 0
while (choice != 7):
    print("\n=== STUDENT RECORDS SYSTEM ===\n")
    print("1. View All Students")
    print("2. Add Student")
    print("3. Search a Student")
    print("4. Remove Student")
    print("5. Total Student")
    print("6. Average marks")
    print("7. Exit")
    choice = int(input("\nEnter Your choice: "))
    if(choice == 1):
        print(25 * "-")
        print(f"{'Name': <10} {'Age': <6} {'marks'}")
        print(25 * "-")

        for student, data in students.items():
                print(f"{student: <10} {data['age']: <6} {data['marks']}")
    
    elif(choice == 2):
        name = input("Enter the name of student: ").strip().title()
        while(name in students.keys()):
            name = input("This student is already here! \nEnter another: ").strip().title()

        age = int(input("Enter the age: "))
        marks = int(input("Enter the marks: "))
        students[name] = {
            "age": age,
            "marks": marks
        }
    elif(choice == 3):
        name = input("Enter the name of Student: ").strip().title()
        if name in students:
            print(f"{name}: ")
            print(f" Age: {students[name]['age']}")
            print(f" marks: {students[name]['marks']}")
        else:
            print("Student not found! ")

    elif(choice == 4):
        name = input("Enter the name of student you want to remove: ").strip().title()
        if name in students:
            students.pop(name)
            print("Removed Successfully! ")
        else:
            print("Student not found! ")

    elif(choice == 5):
        print(f"Total number of students = {len(students)}")

    elif(choice == 6):
        sum = 0
        for student, data in students.items():
            for key, value in data.items():
                if key == "marks":
                    sum += value

        n = len(students)
        print(f"Total number of students = {n}")
        average = float(sum) / float(n)
        print(f"Average marks = {average: .3f}")

    elif(choice == 7):
        print("\nExiting the Program! ")

    else:
        print("Wrong choice! ")
                