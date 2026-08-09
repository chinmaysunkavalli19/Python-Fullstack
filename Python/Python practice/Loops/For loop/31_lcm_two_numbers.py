a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == 0 or b == 0:
    print("LCM: 0")
else:
    start = max(abs(a), abs(b))

    for lcm in range(start, abs(a * b) + 1, start):
        if lcm % abs(a) == 0 and lcm % abs(b) == 0:
            print("LCM:", lcm)
            break
