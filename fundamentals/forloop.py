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

print("-----------------------------------------")
# Inverted Star Pattern
# range(start, stop, step)
# start = 5, stop = 0 (exclusive), step = -1
for star2 in range(5, 0, -1):
    print("*" * star2)

print("-----------------------------------------")
rows = 5
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

print("-----------------------------------------")
