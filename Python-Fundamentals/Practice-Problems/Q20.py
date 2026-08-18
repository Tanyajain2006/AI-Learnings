# Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20< _   – 30%)(0-1lakh print k).

salary = (int)(input("Enter your salary: "))
hra = salary * 0.10
da = salary * 0.05
pf = salary * 0.03

tax = None
if salary < 500000:
    tax = 0
elif salary <= 1000000:
    tax = salary * 0.10
elif salary <= 2000000:
    tax = salary * 0.20
else:
    tax = salary * 0.30

in_hand_salary = salary - (hra + da + pf + tax)
print("In-hand salary:", in_hand_salary)