# Bill & Seating Helper
 
# Define a function using positional arguments
def total_bill(bill_amount, tip_perc):
    # Calculate final bill after adding tip
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")
    return total
 
# Call the function with positional arguments
total_bill(150, 20)
 
 
# Define a recursive function with a docstring
def seating_arrangements(guests):
    '''This is a recursive function to find the number of seating arrangements for guests.'''
 
    # Base case
    if guests == 0 or guests == 1:
        return 1
 
    # Recursive case
    else:
        return guests * seating_arrangements(guests - 1)
 
 
# Access and print the docstring
print(seating_arrangements.__doc__)
 
# Display seating arrangement results
print("Seating arrangements for 1 guest:", seating_arrangements(1))
print("Seating arrangements for 2 guests:", seating_arrangements(2))
print("Seating arrangements for 3 guests:", seating_arrangements(3))
print("Seating arrangements for 5 guests:", seating_arrangements(5))
