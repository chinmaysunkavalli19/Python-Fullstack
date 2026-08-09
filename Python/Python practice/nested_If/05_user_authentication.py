username = input("Enter username: ")
password = input("Enter password: ")

correct_username = "admin"
correct_password = "1234"

if username == correct_username:
    if password == correct_password:
        print("Access granted.")
    else:
        print("Incorrect password.")
else:
    print("Invalid username.")
