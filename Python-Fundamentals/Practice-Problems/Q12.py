import math

radius = (float)(input("Enter the radius of the cylinder: "))
height = (float)(input("Enter the height of the cylinder: "))

volume = math.pi * radius **  2 * height
print("The volume of the cylinder is:", volume)

# cost of volume L milk
total_cost = volume * 40
print("The cost of the milk is:", total_cost, "rupees")