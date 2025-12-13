balance = 1000.00  
pin = '1111'     
is_authenticated = False

print("Welcome to the ATM!")


while not is_authenticated:
    entered_pin = input("Please insert your card and enter your 4-digit PIN: ")
    

    if entered_pin == pin:
        print("Authentication successful.")
        is_authenticated = True
    else:
        print(" Incorrect PIN. Please try again.")


while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change PIN")  
    print("5. Exit")

    choice = input("Choose an option (1-5): ")
    print()

    if choice == '1':

        print(f"Your current balance is: €{balance:.2f}")

    elif choice == '2':
        # Deposit
        try:
            amount = float(input("Enter the amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"€{amount:.2f} has been deposited. New balance: €{balance:.2f}")
            else:
                 print("Deposit amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == '3':
        # Withdraw
        try:
            amount = float(input("Enter the amount to withdraw: "))
            if amount > 0:
                if amount <= balance:
                    balance -= amount
                    print(f"€{amount:.2f} has been withdrawn. New balance: €{balance:.2f}")
                else:
                    print("Insufficient balance.")
            else:
                print("Withdrawal amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    elif choice == '4':
        # Change PIN (WITHOUT FUNCTIONS)
        print("\n--- Change PIN ---")
        
        # 1. Verify old PIN
        old_pin = input("Enter your CURRENT 4-digit PIN: ")
        if old_pin != pin:
            print(" Error: Invalid current PIN.")
            continue # Go back to the main menu

        # 2. Enter and validate new PIN
        while True:
            new_pin = input("Enter your NEW 4-digit PIN: ")
            
            # Validation: 4 digits check using len() and isdigit()
            if len(new_pin) == 4 and new_pin.isdigit():
                pin = new_pin
                print(" PIN successfully changed!")
                break # Exit the inner while loop (new PIN entry)
            else:
                print(" Error: The PIN must contain EXACTLY 4 digits.")
                if input("Try again? (y/n): ").lower() != 'y':
                    print("PIN change cancelled.")
                    break # Exit the inner while loop (new PIN entry)

    elif choice == '5':
        # Exit
        print("Exiting... Thank you for using the ATM! 👋")
        break  # Exit the main loop

    else:
        print("Invalid option. Please try again.")