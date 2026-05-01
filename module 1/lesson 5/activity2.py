selling_price = float(input("Enter the selling price: "))
buying_price = float(input("Enter the buying price: "))

sum = selling_price - buying_price

if selling_price > buying_price:
    print("The item is sold at a profit. Profit amount is ", sum)
elif selling_price < buying_price:
    print("The item is sold at a loss. Loss amount is ", abs(sum))
else:
    print("The item is sold at cost.")