# Conditional Statements Example - If Else

temp = input("Enter the temperature in degrees Celsius: ")
temp = float(temp)

if temp > 25:
    print("It's a warm day.")
    print("Have a ice cream!")
elif temp < 15:
    print("It's a cold day.")
    print("Have a hot Chocolate!")
else:
    print("It's a mild day.")
    print("Have a Sweet Chocolate!")

print("Stay safe and enjoy your day!")
