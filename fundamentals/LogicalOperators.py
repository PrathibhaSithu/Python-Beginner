income = input("Enter your income: ")
income = int(income)

credit_score = input("Enter your credit score: ")
credit_score = float(credit_score)

if income > 50000:
    income = True
else:
    income = False

if credit_score >= 700:
    credit_score = True
else:
    credit_score = False
