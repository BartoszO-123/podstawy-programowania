with open("files.txt", "r") as file:
    for line in file:
        name = line.strip()  # linia bez białych znaków na początku i końcu

        if "." in name:
            parts = name.split(".")

            extension = parts[-1]

            if len(extension) == 4:
                print(name)
