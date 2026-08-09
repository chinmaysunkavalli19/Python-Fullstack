hour = int(input("Enter hour: "))

if 5 <= hour < 12:
    print("Good Morning")
elif 12 <= hour < 17:
    print("Good Afternoon")
elif 17 <= hour < 21:
    print("Good Evening")
elif 0 <= hour < 5 or 21 <= hour < 24:
    print("Good Night")
else:
    print("Invalid hour")
