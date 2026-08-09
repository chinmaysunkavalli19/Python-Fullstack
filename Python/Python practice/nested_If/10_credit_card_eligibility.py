age = int(input("Enter age: "))
income = float(input("Enter income: "))

if age >= 18:
    if income >= 30000:
        print("You are eligible for a credit card.")
    else:
        print("Your income is too low for a credit card.")
else:
    print("You are underage.")
