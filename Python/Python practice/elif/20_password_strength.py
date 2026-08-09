password = input("Enter password: ")

if len(password) >= 8 and any(ch.isupper() for ch in password) and any(ch.isdigit() for ch in password):
    print("Strong password")
else:
    print("Weak password")
