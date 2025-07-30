x = input("X : ")
# This will raise an error because x is a string TypeError: can only concatenate str (not "int") to str
# y = x + 1

print(x)

# print(y)

x = int(x)  # Convert x to an integer
print(x)

float(x)  # Convert x to a float
print(x)

bool(x)  # Convert x to a boolean
# Note: The boolean conversion will return True for any non-empty string
print(x)

str(x)  # Convert x back to a string
# Note: This will not change the value of x, it will just return a new string
print(x)

print(x)

print(x)
