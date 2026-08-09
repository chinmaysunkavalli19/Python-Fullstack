age = int(input("Enter age: "))
matinee = input("Is it a matinee show? ").strip().lower()

if age < 12 or age > 65:
    if matinee == "yes":
        price = 8
    else:
        price = 10
else:
    if matinee == "yes":
        price = 10
    else:
        price = 15

print(f"Ticket price: ${price}")
