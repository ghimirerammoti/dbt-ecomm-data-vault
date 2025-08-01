class Library:
    def __init__(self):
         self.books =[]
    def add_book(self, title):
        self.books.append(title)
    def remove_book(self, title):
        try:
            self.books.remove(title)
        except ValueError:
            print(f"Book '{title}' not found in the library.")
            return
    def search_book(self, title):
        for book in self.books:
            if book == title:
                return book
        return None
    def list_books(self):
        return self.books

