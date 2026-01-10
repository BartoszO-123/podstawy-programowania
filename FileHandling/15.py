file_name = input("File name: ")

try:
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()

        num_characters = len(content)

        words = content.split()
        num_words = len(words)

        lines = content.splitlines()
        num_lines = len(lines)

        print(f"Number of lines: {num_lines}")
        print(f"Number of characters: {num_characters}")
        print(f"Number of words: {num_words}")

except FileNotFoundError:
    print(f"Error: File '{file_name}' does not exist. Check the name and try again.")
