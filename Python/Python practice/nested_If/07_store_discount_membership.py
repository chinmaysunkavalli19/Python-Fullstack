amount = float(input("Enter purchase amount: "))
membership = input("Do you have membership? ").strip().lower()

if amount > 100:
    if membership == "yes":
        discount = 20
    else:
        discount = 10
else:
    discount = 0

final_amount = amount - (amount * discount / 100)
print(f"Discount: {discount}%")
print("Final amount:", final_amount)
