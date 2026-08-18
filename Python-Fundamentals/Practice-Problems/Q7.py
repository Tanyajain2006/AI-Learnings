year = (int)(input("Enter the year: "))
if year % 4 == 0 and year != 100: print(year, "is a leap year.")
else: print(year, "is not a leap year.")