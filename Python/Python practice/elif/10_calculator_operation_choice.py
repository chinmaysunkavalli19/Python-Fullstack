a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation: ")

if operation == "add":
    print("Result:", a + b)
elif operation == "subtract":
    print("Result:", a - b)
elif operation == "multiply":
    print("Result:", a * b)
elif operation == "divide":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")
