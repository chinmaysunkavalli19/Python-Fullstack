num = int(input("Enter a number: "))

if num < 2:
    print("Not Prime")
else:
    divisor = 2
    is_prime = True

    while divisor * divisor <= num:
        if num % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
