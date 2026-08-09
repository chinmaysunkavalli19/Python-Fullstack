age = int(input("Enter age: "))
license_status = input("Do you have a license? ").strip().lower()

if age >= 18:
    if license_status == "yes":
        print("You are eligible to drive.")
    else:
        print("You are not eligible to drive.")
else:
    print("You are not eligible to drive.")
