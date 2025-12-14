def weekday(n):
    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    if 1 <= n <= 7:
        return weekdays[n - 1]
    else:
        return "Invalid day number"


print("Day name for number 1:", weekday(1))
print("Day name for number 4:", weekday(4))
print("Day name for number 7:", weekday(7))
