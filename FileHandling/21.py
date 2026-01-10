import csv


def append_to_file(file_name, data):
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(",".join(data) + "\n")


def split_books():
    with open("books.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            genre = row[2]

            if genre == "Fantasy":
                append_to_file("books_fantasy.txt", row)
            elif genre == "Historical":
                append_to_file("books_historical.txt", row)
            elif genre == "Romance":
                append_to_file("books_romance.txt", row)
            elif genre == "Classic":
                append_to_file("books_classic.txt", row)


split_books()
