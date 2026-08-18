num = (int)(input("Enter a 4-digit number: "))

rev = 0; temp = num
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

print("The reverse of the number is: ", rev)
if num == rev: print("The number is a palindrome.")
else: print("The number is not a palindrome.")