num = (int)(input("Enter a number: "))
if num % 3 == 0 and num % 6 == 0: print("The number is divisible by both 3 and 6.")
elif num % 3 == 0: print("The number is divisible by 3.")
else: print("The number is not divisible by 3 or 6.")