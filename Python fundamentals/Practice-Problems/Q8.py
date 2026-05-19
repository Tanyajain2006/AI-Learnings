import math

x1 = (float)(input("Enter the first x-coordinate: "))
y1 = (float)(input("Enter the first y-coordinate: "))
x2 = (float)(input("Enter the second x-coordinate: "))
y2 = (float)(input("Enter the second y-coordinate: "))

dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("The distance between the two points is: ", dist)