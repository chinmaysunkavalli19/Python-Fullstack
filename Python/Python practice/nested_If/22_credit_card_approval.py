credit_score = int(input("Enter credit score: "))
income = float(input("Enter income: "))

if credit_score >= 700:
    if income >= 30000:
        print("Credit card application approved")
    else:
        print("Credit card application rejected")
else:
    print("Credit card application rejected")
