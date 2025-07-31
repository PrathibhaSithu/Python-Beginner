income = input("Enter your income: ")
income = int(income)

credit_score = input("Enter your credit score: ")
credit_score = float(credit_score)

employed = input("Are you employed? (yes/no): ")
employed = bool(employed.lower() == 'yes')

if income > 50000:
    urincome = True
else:
    urincome = False

if credit_score >= 700:
    urcredit_score = True
else:
    urcredit_score = False

if employed:
    uremployed = True
else:
    uremployed = False


if urincome and urcredit_score and uremployed:
    print("You are eligible for the loan.")
else:
    print("You are not eligible for the loan.")

# Not
if urincome and urcredit_score and not uremployed:
    print("You are eligible for the loan.")
else:
    print("You are not eligible for the loan.")
