while True:
    try:
        hours_parked = float(input("Enter the number of parking hours: "))

        if hours_parked > 0:
            break
        else:
            print("The parking time must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a number for hours.")


parking_fee = 0

if hours_parked <= 2:
    parking_fee = 5
elif hours_parked <= 6:
    parking_fee = 15
else:
    parking_fee = 20


print(f"\nTime parked: {hours_parked} hours")
print(f"Parking fee: {parking_fee:.2f} PLN")
