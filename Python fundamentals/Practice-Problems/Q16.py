tempr = (float)(input("Enter the temperature in Celsius: "))
humidity = (float)(input("Enter the humidity percentage: "))

if tempr >= 30 and humidity >= 90 : print("The weather is hot and humid.")
elif tempr>= 30 and humidity < 90 : print("The weather is hot.")
elif tempr < 30 and humidity >= 90 : print("The weather is humid.")
else: print("The weather is neither hot nor humid.")