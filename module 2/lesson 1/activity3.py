print("Choose your ride:")
print("1. Bike")
print("2. Car")

choice = int(input("Enter the number corresponding to your choice: "))

if choice == 1:
    print("What type of bike do you want?")
    print("1. Scooter")
    print("2. Motorcycle")

    choice2 = int(input("Enter the number corresponding to your choice: "))
    if choice2 == 1:
        print("You have chosen a Scooter.")
    elif choice2 == 2:
        print("You have chosen a Motorcycle.")
    else:
        print("Invalid input.")

elif choice == 2:
    print("What type of car do you want?")
    print("1. Sedan")
    print("2. SUV")

    choice2 = int(input("Enter the number corresponding to your choice: "))
    if choice2 == 1:
        print("You have chosen a Sedan.")
    elif choice2 == 2:
        print("You have chosen an SUV.")
    else:
        print("Invalid input.")

else:
        print("Invalid input. Please choose either 1 or 2.")