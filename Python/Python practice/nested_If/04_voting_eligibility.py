age = int(input("Enter age: "))
citizen = input("Are you a citizen? ").strip().lower()

if age >= 18:
    if citizen == "yes":
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
else:
    print("You are not eligible to vote.")
