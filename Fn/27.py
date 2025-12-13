def replace_spaces(sentence):
    return sentence.replace(" ", "")


print(f"{replace_spaces('integrated development environment')} returns")
print(f'"{replace_spaces("integrated development environment")}"')

print("\n" + "-" * 20 + "\n")

print(
    f"{replace_spaces('A programming language is a system of notation for writing computer programs')} returns"
)
print(
    f'"{replace_spaces("A programming language is a system of notation for writing computer programs")}"'
)
