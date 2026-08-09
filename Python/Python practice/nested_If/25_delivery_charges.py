distance = float(input("Enter distance: "))
amount = float(input("Enter order amount: "))

if amount >= 500:
    charge = 0
else:
    if distance <= 5:
        charge = 20
    elif distance <= 10:
        charge = 50
    else:
        charge = 100

print(f"Delivery charge: ${charge}")
