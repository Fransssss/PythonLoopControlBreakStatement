# loop control statement
# Break    - stop loop

print("\nLoop Control Statement")
print("1 X\n2 X\n3 X\nQ quit")
choice = input("Choose one from these 3 numbers to answer a question: ")

while choice != "Q" and choice != "q":     # while input is not q/Q
    if choice == "1":
        name = input("\nWhat is your name: ")
        print("Hello " + name)
        break                              # get out of the loop - no need to wait until user input q/Q
    elif choice == "2":
        age = int(input("\nHow old are you: "))
        print("You are " + str(age) + " y/d")
        break
    elif choice == "3":
        color = input("\nwhat is your favorite color: ")
        print("Your favorite color is " + color)
        break
    else:
        print("\n[Invalid choice]\n")

    print("1 X\n2 X\n3 X\nQ quit")
    choice = input("Choose one from these 3 numbers to answer a question: ")
