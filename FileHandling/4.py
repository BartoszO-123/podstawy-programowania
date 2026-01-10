total_words = 0
filename = "pets.txt"

with open(filename, "r") as file:
    for line in file:
        print(line, end="")

        words = line.split()

        total_words = total_words + len(words)

print()
print("Number of words:", total_words)
