num = int(input("Enter number: "))

if num % 2 == 0:
    print(num, "is even")
    if num > 10:
        print(num, "is greater than 10")
    else:
        print(num, "is not greater than 10")
else:
    print(num, "is odd")
