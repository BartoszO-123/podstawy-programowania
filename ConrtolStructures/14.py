###
# Calculates the number of days in a month
#
month = int(input("Enter month number (1..12)"))

if month in (1, 3, 5, 7, 8, 10, 12):
    days = 31  ## months with 31 days
elif month in (4, 6, 9, 11):
    days = 30  ## months with 30 days
else:
    days = 28
## February 28 days

print(f"Month {month} has {days} days")
