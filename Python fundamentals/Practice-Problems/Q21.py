choice = None

while choice != 4:
    print("Menu:")
    print("Choice 1: Convert cm to ft")
    print("Choice 2: Convert km to miles")
    print("Choice 3: Convert USD to INR")
    print("Choice 4: Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        cm = float(input("Enter the length in centimeters: "))
        ft = cm / 30.48
        print(f"{cm} cm is equal to {ft:.2f} ft.")
    elif choice == 2:
        km = float(input("Enter the distance in kilometers: "))
        miles = km * 0.621371
        print(f"{km} km is equal to {miles:.2f} miles.")
    elif choice == 3:
        usd = float(input("Enter the amount in USD: "))
        inr = usd * 82.75
        print(f"{usd} USD is equal to {inr:.2f} INR.")
    elif choice == 4:
        print("Exiting the program. Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        choice = None  # Reset choice to continue the loop for valid input