from ebook import EBook

# 1. Create a book
my_book = EBook("The Great Gatsby", "F. Scott Fitzgerald", 180)

# 2. Open the book
my_book.open_book()

# 3. Display status
my_book.display_status()

# 4. Read a few pages
my_book.next_page()
my_book.next_page()
my_book.next_page()

# 5. Display status again
my_book.display_status()

# 6. Close the book
my_book.close_book()

# 7. Try to read while closed
my_book.next_page()