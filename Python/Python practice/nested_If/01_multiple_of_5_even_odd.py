num = int(input("Enter a number: "))

if num % 5 == 0:
    if num % 2 == 0:
        print(f"{num} is a multiple of 5 and it is even")
    else:
        print(f"{num} is a multiple of 5 and it is odd")
else:
    print("its not multiple of 5")
