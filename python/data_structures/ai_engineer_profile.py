profile = {
    "name": "",
    "age": "",
    "university": "",
    "skills": [],
    "languages": ["python"],
    "projects": [],
    "github": "",
    "goal": "To be an end to end AI Engineer"
}

profile["name"] = input("Enter your name: ").strip().title()
profile["age"] = int(input("Enter your age: "))
profile["university"] = input("Enter the name of your university: ").strip().title()
profile["skills"] = [input("Enter your first skill: "), 
                     input("Enter your second skill: "),
                     input("Enter your third skill: ")]
profile["languages"].append(input("Enter a programming language you learned: "))
profile["projects"].extend(str(input("Enter two or more projects you made: ")))
profile["github"] = input("Drop your github link here: ").strip()

print(profile)

