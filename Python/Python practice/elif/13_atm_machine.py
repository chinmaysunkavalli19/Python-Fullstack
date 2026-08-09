balance = 10000
choice = input("Enter choice: ").strip().lower()

if choice == "balance":
    print("Your balance is:", balance)
elif choice == "withdraw":
    amount = float(input("Enter amount: "))
    if amount <= 0:
        print("Invalid amount")
    elif amount <= balance:
        balance -= amount
        print("Withdrawal successful")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")
else:
    print("Invalid choice")
