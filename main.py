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
<<<<<<< HEAD
        print(f"Your current balance is: {balance} birr.")
=======
        print(f"Your current balance is {balance} Birr")
>>>>>>> cba7947 (Added USSD menu)

    # -------------------------------
    # Group 2: Buy Data
    elif option == "2":
<<<<<<< HEAD
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
=======
        data_cost = 20
        if balance >= data_cost:
            balance -= data_cost
            print("You have successfully bought data.")
            print(f"Remaining balance: {balance} Birr")
        else:
            print("Insufficient balance to buy data.")
>>>>>>> cba7947 (Added USSD menu)

    # -------------------------------
    # Group 3: Buy Airtime
    elif option == "3":
<<<<<<< HEAD
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
=======
        airtime_cost = int(input("Enter airtime amount: "))
        if airtime_cost <= balance:
            balance -= airtime_cost
            print(f"Airtime of {airtime_cost} Birr purchased successfully.")
            print(f"Remaining balance: {balance} Birr")
        else:
            print("Insufficient balance to buy airtime.")
>>>>>>> cba7947 (Added USSD menu)

    # -------------------------------
    # Group 4: Exit
    elif option == "4":
<<<<<<< HEAD
        print("Thank you for using our service. Goodbye!")
        break

    # -------------------------------
    # Invalid Input
    else:
        print("Invalid option. Please try again.")

=======
        print("Thank you for using the USSD service.")
        break
    else:
        print("Invalid option. Please try again.")
>>>>>>> cba7947 (Added USSD menu)
