# Given an email id, find its username

email = input("Enter your enmail: ")
while '@' not in email:
    print("Invalid email")
    email = input("Enter correct email: ")

username = email.split('@')
print(username)
print("Username is:", username[0])