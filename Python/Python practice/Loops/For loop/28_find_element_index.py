items = [10, 20, 30, 40]
element = int(input("Enter element: "))
found = False

for i in range(len(items)):
    if items[i] == element:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")
