email = input("Enter your email: ")
while("@" not in email):
    email = input("Invalid email, please enter correct email: ")
    
password = input("Enter your password: ")


if email == "campusx@gmail.com" and password == "12345":
    print("Login successful!")
elif email == "campusx@gmail.com":
    print("Incorrect password")
    password = input("Enter your password again: ")
    if password == "12345":
        print("Login successful!")
    else: print("Still incorect")
else: print("Invalid credentials")