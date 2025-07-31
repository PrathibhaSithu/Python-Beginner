successful = False
for number in range(4):
    print("Line", number + 1, (number + 1) * "*")
    if successful:
        print("Success on line no: " + str(number))
        break
    else:
        print("No success found in the loop")
