class BookSearcher:
    def __init__(self, all_books):
        self.books = all_books

    def search_by_city(self, city):
        results = []
        for book in self.books.values():
            results += book.city_directory.get(city, [])
        return results