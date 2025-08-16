#  For loop

for i in range(5):
    print(i)

#  While loop

count = 0
while count < 5:
    print(count)
    count += 1

#  Break statement
for i in range(5):
    if i == 3:
        break
    print("Break", i)

#  Continue statement
for i in range(5):
    if i == 2:
        continue
    print("Continue", i)
