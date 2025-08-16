command = ""

while command.lower() != "exit":
    command = input("Enter a command (type 'exit' to quit): ")
    print("You entered:", command)


while True:
    command = input("> ")
    print("You entered:", command)
    if command.lower() == "exit":
        break
