vehicle_type = input("Enter vehicle type: ").strip().lower()
emissions = input("Enter emissions status: ").strip().lower()

if vehicle_type == "car":
    if emissions == "clean":
        fee = 100
    else:
        fee = 200
elif vehicle_type == "truck":
    if emissions == "clean":
        fee = 200
    else:
        fee = 300
else:
    fee = 0
    print("Invalid vehicle type")

if fee > 0:
    print(f"Registration fee: ${fee}")
