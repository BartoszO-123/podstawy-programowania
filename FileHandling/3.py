filename = "car_park.txt"


def read_from_file(name):
    with open(name) as file:
        content = file.read()
    return content


file_content = read_from_file(filename)
file_lines = file_content.splitlines()   # dzieli tekst na linie tam gdzie enter był klikniety

total = 0


for line in file_lines:
    total = total + int(line) # konwertuje string na int i dodaje do total

print("Total cars parked:", total)
