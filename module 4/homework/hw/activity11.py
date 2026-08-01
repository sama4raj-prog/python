snackbox1 = {"chips", "cookies", "candy", "soda"}
snackbox2 = {"candy", "soda", "juice", "nuts", "soda","soda"}

print (f"Snackbox 1: {snackbox1}")
print (f"Snackbox 2: {snackbox2}")

snackbox2.add("chocolate")
print (f"Snackbox 2 after adding chocolate: {snackbox2}")

common_snacks = snackbox1.intersection(snackbox2)
print (f"Common snacks in both boxes: {common_snacks}")

import array as arr

snack_counts = arr.array('i', [2, 3, 4, 5])
print (snack_counts)

snack_counts.insert(0, 1)
print (snack_counts)
snack_counts.append(6)
print (snack_counts)

snack_counts.reverse()
print (snack_counts)

print (f"Snackbox 1: {snackbox1}")
print (f"Snackbox 2: {snackbox2}")
print (f"Final snack count: {snack_counts}")
