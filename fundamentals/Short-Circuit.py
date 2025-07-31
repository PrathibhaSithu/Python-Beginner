high_income = True
good_credit = True
Student = True

if high_income and good_credit and not Student:
    print("Eligible for loan")
# else:
#     print("Not eligible for loan")

if high_income or good_credit or not Student:
    print("Eligible for loan")
# else:
#     print("Not eligible for loan")
