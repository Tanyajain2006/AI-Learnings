a = (int)(input("Enter the first number: "))
b = (int)(input("Enter the second number: "))

print(f"Before swapping: a = {a}, b = {b}")

# Method 1
a, b = b, a
print(f"After swapping (Method 1): a = {a}, b = {b}")

# Method 2
temp = a
a = b
b = temp
print(f"After swapping (Method 2): a = {a}, b = {b}")