cost_price = float(input("Enter the cost price: "))
sell_price = (float)(input("Enter the sell price: "))

if sell_price > cost_price: print("Profit")
elif sell_price < cost_price: print("Loss")
else: print("No profit, no loss")