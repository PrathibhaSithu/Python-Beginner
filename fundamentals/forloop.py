# Syntax for a for loop in Python
#   for variable in sequence:
#   code block to run on each item


for number in range(4):
    print("Line", number + 1, (number + 1) * "*")

for pattern1 in range(4):
    print((pattern1 + 1) * "!")

for pattern2 in range(1, 4):
    print((pattern2 + 1) * "####")

for pattern3 in range(1, 10, 2):
    print("Line", pattern3 + 1, (pattern3 + 1) * "^")

# Star Pattern
for star1 in range(1, 6):
    print("*" * star1)
