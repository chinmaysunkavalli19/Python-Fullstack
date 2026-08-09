num = int(input("Enter number: "))
num = abs(num)
total = 0

for digit in str(num):
    total += int(digit)

print("Sum of digits:", total)
