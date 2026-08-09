num = int(input("Enter number: "))
end = int(input("Enter range: "))
multiples = []

for i in range(num, end + 1, num):
    multiples.append(i)

print("Multiples:", multiples)
