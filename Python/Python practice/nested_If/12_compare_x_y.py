x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x > y:
    print("x is greater than y")
    if x > 15:
        print("x is also greater than 15")
    else:
        print("x is not greater than 15")
else:
    print("x is not greater than y")
