num = int(input("Enter a number: "))

root = round(abs(num) ** (1 / 3))

if root ** 3 == abs(num):
    print("Perfect Cube")
