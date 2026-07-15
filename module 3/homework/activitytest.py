user_input = input("Enter the number of month between 1-12 (if all then enter 'all'): ")

months = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}

if user_input.lower() == 'all':
    print("You have selected all months.")
    for month_name in months.values():
        print(month_name)

elif user_input in months:
    print(f"{months[user_input]}.")
else:
    print("Invalid input. Please enter a valid month number between 1-12 or 'all'.")