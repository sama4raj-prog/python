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