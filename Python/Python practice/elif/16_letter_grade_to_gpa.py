grade = input("Enter grade: ").strip().upper()

if grade == "A":
    print("GPA: 4.0")
elif grade == "B":
    print("GPA: 3.0")
elif grade == "C":
    print("GPA: 2.0")
elif grade == "D":
    print("GPA: 1.0")
elif grade == "F":
    print("GPA: 0.0")
else:
    print("Invalid grade")
