###
# Checks if the given day number of the month is correct
#
month = int(input("Enter month number (1..12): "))
day = int(input("Enter the day number of the month: "))

message = f"Day {day} for the month {month}"
day_ok = False

if month in (1, 3, 5, 7, 8, 10, 12):
    if day >= 1 and day <= 31:
        day_ok = True
elif month in (4, 6, 9, 11):
    if day >= 1 and day <= 30:
        day_ok = True
elif month == 2:
    if day >= 1 or day <= 28:
        day_ok = True
else:
    pass


if day_ok:
    print(f"{message} is correct")
else:
    print(f"{message} is not correct")
