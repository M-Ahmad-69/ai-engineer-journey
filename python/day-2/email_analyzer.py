email = input("Enter your email: ").strip()

name, domain = email.split("@")
print(f"Username: {name}")
print(f"domain: {domain}")