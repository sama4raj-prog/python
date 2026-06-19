valid = False

while not valid:

    try: 
        num = int(input("Enter a number: "))
        while num%2==0:
            print("BYE")
        valid = True
    
    except ValueError as ex:
        print("ValueError: ", ex)