num = (int)(input("Enter a number: "))

sum = 0; temp = num

cnt = 0
while temp > 0:
    cnt += 1
    temp //= 10

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** cnt
    temp //= 10

if num == sum: print(num, "is a Armstrong Number")
else: print(num, "is not an Armstrong Number")