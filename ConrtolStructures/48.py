for number in range(1, 31):
    output = ""

    if number % 15 == 0:
        output = "BINGO"

    elif number % 3 == 0:
        output = "THREE"

    elif number % 5 == 0:
        output = "FIVE"

    else:
        output = str(number)

    print(output, end=" ")

print()
