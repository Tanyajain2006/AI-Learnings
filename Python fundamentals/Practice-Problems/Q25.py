num1 = (int)(input("Enter the first number: "))
num2 = (int)(input("Enter the second number: "))

temp = 0
for i in range(0, num2):
    temp += num1

print("The product of the two numbers is:", temp)