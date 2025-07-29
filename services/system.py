# services/system.py

from services.address_book import ContactBook

class BookSystem:
    def __init__(self):
        self.books = {}

    def create_book(self, book_name):
        if book_name in self.books:
            print(f"⚠️ Address book '{book_name}' already exists.")
        else:
            self.books[book_name] = ContactBook(book_name)
            print(f" Created address book '{book_name}'.")

    def get_book(self, name):
        if name in self.books:
            return self.books[name]
        raise ValueError(f" Address book '{name}' not found.")

    def remove_book(self, name):
        if name in self.books:
            del self.books[name]
            print(f"Deleted address book '{name}'.")
        else:
            print(f"Address book '{name}' does not exist.")

    def list_books(self):
        return self.books