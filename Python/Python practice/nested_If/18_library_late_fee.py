days = int(input("Enter overdue days: "))
book_type = input("Enter book type: ").strip().lower()

if days <= 0:
    fee = 0
else:
    if book_type == "regular":
        fee = days * 1
    elif book_type == "reference":
        fee = days * 2
    else:
        fee = 0
        print("Invalid book type")

print(f"Late fee: ${fee}")
