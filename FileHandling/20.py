file_name = "powers.txt"


with open(file_name, "w") as file:
    for i in range(1, 101):
        square = i**2
        cube = i**3

        line = f"{i},{square},{cube}"

        print(line)

        file.write(line + "\n")

print(f"\nDone! Results have been saved to file: {file_name}")
