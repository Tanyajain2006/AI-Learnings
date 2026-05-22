num = (int)(input("Enter a number: "))

def factorial(n):
    if n == 0 or n == 1: return 1
    else:
        ans = 1
        for i in range(2, n + 1):
            ans *= i
        return ans
    
print("The factorial of the number is:", factorial(num))