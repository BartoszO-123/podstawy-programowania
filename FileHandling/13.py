file_name = "it_company.csv"

try:
    with open(file_name, "r") as file:
        counter = 0

        for line in file:
            print(line, end="")
            counter = counter + 1

            if counter == 5:
                input("\nPress Enter key...")

                counter = 0

except FileNotFoundError:
    print("Error: File it_company.csv not found")
