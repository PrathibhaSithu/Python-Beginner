# Print to Console
print("Hello, World!")

# Variable Assignment
x = 10
y = 5
z = x + y

# Commenting
# This is a single-line comment

"""
This is a multi-line comment
spanning multiple lines
"""

# Input from user
name = input("Enter your name: ")
age = input("Enter your age: ")

# check Datatype
print(type(name))
print(type(age))
type(x)

# Type Casting
int("10"), float(10.5), str(100)

x = 5

print(1 < x < 10)        # True
print(10 > x >= 5)       # True
print(5 == x < 6)        # True
print(5 == x == 6)       # False

# Control Flow

# If
if x > 10:
    print("x is greater than 10")

# If Else
if x > 10:
    print("x is greater than 10")
else:
    print("x is not greater than 10")

# If Elif Else
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is smaller than 10")
