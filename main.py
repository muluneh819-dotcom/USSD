balance = 100  # Starting balance

while True:
    print("\nUSSD Menu:")
    print("1. Check Balance")
    print("2. Buy Data")
    print("3. Buy Airtime")
    print("4. Exit")

    option = input("Enter option: ")

    # -------------------------------
    # Group 1: Check Balance
    if option == "1":
        print(f"Your current balance is: {balance} birr.")

    # -------------------------------
    # Group 2: Buy Data
    elif option == "2":
        print("Data packages:")
        print("1. 200MB = 25 birr")
        print("2. 500MB = 50 birr")
        print("3. 1GB = 100 birr")

        choice = input("Choose a data package (1-3): ")

        if choice == "1" and balance >= 25:
            balance -= 25
            print("You bought 200MB of data.")
        elif choice == "2" and balance >= 50:
            balance -= 50
            print("You bought 500MB of data.")
        elif choice == "3" and balance >= 100:
            balance -= 100
            print("You bought 1GB of data.")
        else:
            print("Insufficient balance or invalid choice.")

        print(f"Remaining balance: {balance} birr.")

    # -------------------------------
    # Group 3: Buy Airtime
    elif option == "3":
        try:
            amount = float(input("Enter airtime amount: "))
            if amount <= balance:
                balance -= amount
                print(f"You bought {amount} birr airtime.")
                print(f"Remaining balance: {balance} birr")
            else:
                print("Insufficient balance.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # -------------------------------
    # Group 4: Exit
    elif option == "4":
        print("Thank you for using our service. Goodbye!")
        break

    # -------------------------------
    # Invalid Input
    else:
        print("Invalid option. Please try again.")

