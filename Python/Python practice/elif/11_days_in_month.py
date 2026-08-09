month = int(input("Enter month number: "))

if month == 2:
    print("Number of days: 28")
elif month in (4, 6, 9, 11):
    print("Number of days: 30")
elif month in (1, 3, 5, 7, 8, 10, 12):
    print("Number of days: 31")
else:
    print("Invalid month")
