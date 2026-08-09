age = int(input("Enter age: "))
height = float(input("Enter height: "))

if age < 12:
    if height < 4:
        price = 10
    else:
        price = 15
else:
    if height < 4:
        price = 15
    else:
        price = 20

print(f"Ticket price: ${price}")
