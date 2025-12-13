correct_pin = "0805"
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    user_input = input("Enter the PIN code: ")

    if user_input == correct_pin:
        print("PIN Accepted. Welcome!")
        break
    else:
        print("Incorrect...")

        if attempt == max_attempts:
            print("Sorry, your payment card has been blocked.")
