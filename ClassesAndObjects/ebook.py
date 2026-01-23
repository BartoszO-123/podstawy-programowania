class EBook:
    def __init__(self, title, author, total_pages):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = 1
        self.is_open = False

    def open_book(self):
        self.is_open = True
        print(f"Opening '{self.title}'...")

    def close_book(self):
        self.is_open = False
        print(f"Closing '{self.title}'...")

    def next_page(self):
        if self.is_open:
            if self.current_page < self.total_pages:
                self.current_page += 1
                print(f"Moved to page {self.current_page}.")
            else:
                print("You are already on the last page.")
        else:
            print("Error: You cannot read. The book is closed.")

    def previous_page(self):
        if self.is_open:
            if self.current_page > 1:
                self.current_page -= 1
                print(f"Moved back to page {self.current_page}.")
            else:
                print("You are on the first page.")
        else:
            print("Error: You cannot read. The book is closed.")

    def display_status(self):
        status = "Open" if self.is_open else "Closed"
        print("\n--- Book Status ---")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Total Pages: {self.total_pages}")
        print(f"Current Page: {self.current_page}")
        print(f"Status: {status}")
        print("-------------------\n")