# Reads from file, line by line
#
n = 1
filename = "countries.txt"
with open(filename, "r") as file:
    for line in file:
        print(n, ". ", line, sep="", end="")

        n = n + 1
