pswrd = input("Please Enter your password: ")

print(f"password: {"*" * (len(pswrd) - 3)} {pswrd[-3 : ]}")