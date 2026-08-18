# Narcissist number = sum of digits raised to the power of number of digits

num = (int)(input("Enter a 4-digit number: "))
while num < 1000 or num > 9999:
    print("Please enter a 4-digit number.")
    num = (int)(input("Enter a 4-digit number: "))

sum = 0, temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 4
    temp //= 10

if num == sum: print(num, "is a Narcissist Number")
else: print(num, "is not a Narcissist Number")

# armstrong number is a narcissist number.