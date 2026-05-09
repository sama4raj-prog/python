medical_cause = input("Do you have any medical cause? (yes/no): ").lower()

if medical_cause == "no" :
    attendance = int(input("Enter your attendance: "))
    if attendance >= 75:
        print("You are allowed to sit in the exam.")
    else:
        print("You are not allowed to sit in the exam.")
else:
    print("You are allowed to sit in the exam.")