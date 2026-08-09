ch = input("Enter a character: ")

if ch.isalpha():
    if ch.isupper():
        print("Uppercase letter")
    else:
        print("Lowercase letter")
else:
    print("Not a letter")
