seven_wonders = [
    "Great Wall of China",
    "Petra",
    "Christ the Redeemer",
    "Machu Picchu",
    "Chichen Itza",
    "Roman Colosseum",
    "Taj Mahal",
]


file_name = "seven_wonders.txt"


seven_wonders.sort()


with open(file_name, "w") as file:
    for item in seven_wonders:
        file.write(item + "\n")

print(f"List has been written to file {file_name}.")
