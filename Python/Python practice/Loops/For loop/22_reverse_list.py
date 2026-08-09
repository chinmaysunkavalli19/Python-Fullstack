items = [1, 2, 3, 4, 5]
reversed_list = []

for i in range(len(items) - 1, -1, -1):
    reversed_list.append(items[i])

print("Reversed list:", reversed_list)
