amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount = 20
elif amount >= 1000:
    discount = 10
else:
    discount = 0

final_price = amount - (amount * discount / 100)
print(f"Discount: {discount}%")
print("Final price:", final_price)
