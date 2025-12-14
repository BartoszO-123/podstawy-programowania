cinema_seats = [
    ["A", "A", "B", "A", "A"],
    ["A", "B", "B", "A", "A"],
    ["A", "A", "A", "A", "B"],
    ["B", "A", "A", "A", "A"],
    ["A", "B", "A", "A", "A"],
]


def seats_total(seats):
    total = 0
    for row in seats:
        total += len(row)
    return total


def seats_available(seats):
    count = 0
    for row in seats:
        count += row.count("A")
    return count


def seats_booked(seats):
    count = 0
    for row in seats:
        count += row.count("B")
    return count


def seat_status(seats, row, place):
    row_index = row - 1
    place_index = place - 1

    if 0 <= row_index < len(seats) and 0 <= place_index < len(seats[0]):
        status_char = seats[row_index][place_index]
        return "Available" if status_char == "A" else "Booked"
    else:
        return "Invalid seat"


total = seats_total(cinema_seats)
available = seats_available(cinema_seats)
booked = seats_booked(cinema_seats)

print("\nCINEMA INFORMATION TABLE")
print("========================")
print("Total seats:", total)
print("Seats available:", available)
print("Seats booked:", booked)

print(f"Seat in row 1, place 1: {seat_status(cinema_seats, 1, 1)}")
print(f"Seat in row 5, place 5: {seat_status(cinema_seats, 5, 5)}")
print(f"Seat in row 3, place 5: {seat_status(cinema_seats, 3, 5)}")
