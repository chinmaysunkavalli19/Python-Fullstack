num = int(input("Enter number: "))
step = int(input("Enter step: "))
factorial = 1

for i in range(1, num + 1, step):
    factorial *= i

print("Factorial:", factorial)
