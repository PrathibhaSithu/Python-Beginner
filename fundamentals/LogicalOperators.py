income = input("Enter your income: ")
income = int(income)

credit_score = input("Enter your credit score: ")
credit_score = float(credit_score)

if income > 50000:
    urincome = True
else:
    urincome = False

if credit_score >= 700:
    urcredit_score = True
else:
    urcredit_score = False


if urincome and urcredit_score:
    print("You are eligible for the loan.")
else:
    print("You are not eligible for the loan.")
