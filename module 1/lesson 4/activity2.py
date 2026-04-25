#Taking total amount as input from user
Amount =int(input("Please enter the amount: "))

note_100 = Amount//100
note_50 = (Amount%100)//50
note_10 = ((Amount%100)%50)//10

print("Notes of 100 taka: ", note_100)
print("Notes of 50 taka: ", note_50)
print("Notes of 10 taka: ", note_10)