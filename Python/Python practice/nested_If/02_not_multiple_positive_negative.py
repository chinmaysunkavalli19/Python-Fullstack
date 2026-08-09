num = int(input("Enter a number: "))

if num % 5 == 0:
    print(f"{num} is a multiple of 5")
else:
    if num > 0:
        print(f"{num} is not a multiple of 5 and it is positive")
    else:
        print(f"{num} is not a multiple of 5 and it is negative")
