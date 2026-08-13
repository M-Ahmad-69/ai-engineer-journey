def menu():
    print("1. Write notes")
    print("2. Read all notes")
    print("3. Add a note")
    print("4. Read line by line")
    print("5. Exit")

def write():
    with open("notes.txt", "w") as file:
        file.write(input("Enter your note: ") + "\n")

def read_all():
    with open("notes.txt", "r") as file:
        print(file.readlines())

def add():
    with open("notes.txt", "a") as file:
        file.write(input("Enter a note: "))

def read():
    with open("notes.txt", "r") as file:
        for line in file:
            print(line, end="")

while True:
    menu()

    choice = input("Enter choice: ")
    if choice == "1":
        write()
    elif choice == "2":
        read_all()
    elif choice == "3":
        add()
    elif choice == "4":
        read()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
    