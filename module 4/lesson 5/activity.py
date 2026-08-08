item = ["pencil", "notebook", "eraser", "marker"]
stock_counts = [12,0,8,5,3]

inventory = {item : count for item, count in zip(item, stock_counts)}
print("Full inventory:", inventory)

in_stock_items = [item for item in item if inventory[item] > 0]
print("Items in stock:", in_stock_items)

chosen_item = input("What item do you want to buy? ->")
if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(f"{chosen_item} is out of stock! Stopping the checker.")
    exit()
    
prices = [10,5,40,15,20]
markup = int(input("Enter the markup amount to add to every price: "))

markedup_prices = list(map(lambda p : p + markup,prices))
print("Marked up prices:", markedup_prices)

item_index = item.index(chosen_item)
chosen_price = markedup_prices[item_index]
print(f"The price of {chosen_item} after markup is: ${chosen_price}")

inventory[chosen_item] -= 1
print(f"{chosen_item} purchased! Remaining stock: {inventory[chosen_item]}")