food = input("Enter food: ").strip().lower()

if food == "burger":
    fries = input("Do you want fries? ").strip().lower()
    if fries == "yes":
        print("Your order: Burger with Fries")
    else:
        print("Your order: Burger")
elif food == "pizza":
    cheese = input("Do you want extra cheese? ").strip().lower()
    if cheese == "yes":
        print("Your order: Pizza with Extra Cheese")
    else:
        print("Your order: Pizza")
else:
    print("Invalid food choice")
