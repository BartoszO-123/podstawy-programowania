rows = 7
columns = 7
max_numbers = 49

i = 1
while i <= rows:
    j = 0
    while j < columns:
        number = i + (j * rows)

        if number <= max_numbers:
            print(f"{number: <3}", end="")

        j += 1

    print()
    i += 1
