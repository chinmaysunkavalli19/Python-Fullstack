gpa = float(input("Enter GPA: "))
activities = int(input("Enter number of activities: "))

if gpa > 3.5:
    if activities >= 3:
        print("Scholarship awarded")
    else:
        print("Scholarship not awarded")
else:
    print("Scholarship not awarded")
