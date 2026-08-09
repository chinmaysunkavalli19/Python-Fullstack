score = float(input("Enter performance score: "))
years = int(input("Enter years of service: "))

if score >= 90:
    performance = "Excellent"
    bonus = 20000 if years >= 5 else 15000
elif score >= 70:
    performance = "Good"
    bonus = 10000 if years >= 5 else 7000
else:
    performance = "Average"
    bonus = 5000 if years >= 5 else 3000

print("Performance:", performance)
print("Bonus:", bonus)
