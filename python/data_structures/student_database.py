database = {
    "Ahmad": {
        "age": 19,
        "cgpa": 3.7
    },
    "Bilal": {
        "age": 15,
        "cgpa": 3.2
    },
    "Ali": {
        "age": 17,
        "cgpa": 2.0
    }
}

student = input("Enter student name: ").strip().title()
database[student] = {"age": int(input("Enter age")),
                     "cgpa": float(input("Enter cgpa: "))}

database["Ahmad"]["cgpa"] = float(input("Enter cgpa: "))

database["Ali"]["department"] = input("Enter department: ").strip().title()

database.pop(student, None)

print(database)