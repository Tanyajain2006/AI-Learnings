heads = (int)(input("Enter the number of heads: "))
legs = (int)(input("Enter the number of legs: "))

dogs = None; chickens = None
if heads < 0 or legs < 0: print("Invalid input: Number of heads and legs cannot be negative.")
elif legs % 2 != 0: print("Invalid input: Number of legs must be even.")
else:
    dogs = legs // 4
    chickens = heads - dogs
    if chickens < 0 or dogs < 0: print("No valid solution exists with the given number of heads and legs.")
    else: print(f"Number of chickens: {chickens}, Number of dogs: {dogs}")