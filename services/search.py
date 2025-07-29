class BookSearcher:
    def __init__(self, all_books):
        self.books = all_books

    def search_by_city(self, city):
        results = []
        for book in self.books.values():
            results += book.city_directory.get(city, [])
        return results
    def search_by_state(self, state):
        results = []
        for book in self.books.values():
            results += book.state_directory.get(state, [])
        return results
#UC7 alreayd done above
#UC8 alreayd done above
    def count_by_city(self, city):
        count = 0
        for book in self.books.values():
            count += len(book.city_directory.get(city, []))
        return count