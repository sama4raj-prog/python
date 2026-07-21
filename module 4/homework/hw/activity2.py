# Define a function with no arguments to greet the customer
def greet_customer():
    print("Welcome to the Art Supplies Store!")
    print("Get your colours, brushes, and paper here.")
 
# Call the greet_customer function
greet_customer()
 
# Ask for the price per item and the number of items bought
price_per_item = float(input("Enter the price per art item in dollars: "))
items_bought = int(input("Enter the number of art items bought: "))
 
# Define a function that takes arguments and returns the total cost
def calculate_total(price, items):
    total = price * items
    return total
 
# Call calculate_total and store the value it returns
total_cost = calculate_total(price_per_item, items_bought)
 
# Use a built-in function to round the total, then print it
rounded_total = round(total_cost, 2)
print("Total Cost:", rounded_total)
 
# Ask how much money the customer paid
amount_paid = float(input("Enter the amount paid by the customer: "))
 
# Define a function that takes arguments and returns the change due
def calculate_change(paid, total):
    change = paid - total
    return change
 
# Call calculate_change and store the value it returns
change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)
 
# Define a function that returns a thank you message based on items bought
def thank_you_message(items):
    if items >= 5:
        return "Great choice! You picked many art supplies for your project."
    else:
        return "Thanks for shopping at the art supplies store!"
 
# Call thank_you_message and store the value it returns
closing_message = thank_you_message(items_bought)
 
# Print the final art supplies receipt
print("")
print("===== ART SUPPLIES BILL =====")
print("Price Per Item:", price_per_item)
print("Items Bought:", items_bought)
print("Total Cost:", rounded_total)
print("Amount Paid:", amount_paid)
print("Change Due:", rounded_change)
print(closing_message)
print("=============================")
