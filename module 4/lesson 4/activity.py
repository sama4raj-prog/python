basket1 = {"apple", "banana", "mango", "jackfruit"}
basket2 = {"mango", "kiwi", "banana", "kiwi"}

print (f"Basket 1: {basket1}")
print (f"Basket 2: {basket2}")

basket2.add("oranges")
print (f"Basket 2 after adding oranges: {basket2}")

common_fruits = basket1.intersection(basket2)
print (f"Common fruits in both baskets: {common_fruits}")

import array as arr

fruit_counts = arr.array('i', [5, 3, 2, 4])
print (fruit_counts)

fruit_counts.insert(0, 1)
print (fruit_counts)
fruit_counts.append(6)
print (fruit_counts)

fruit_counts.reverse()
print (fruit_counts)