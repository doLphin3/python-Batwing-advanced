class BookDB:
    books = [{"name": "test_book", "author": "test_author"}]

    def get_all(self):
        return self.books

    def retrieve_by_name(self, name):
        for book in self.books:
            if book["name"] == name:
                return book
        return None

    def add(self, name, author):
        book_already_exists = False
        for book in self.books:
            if book["name"] == name:
                book_already_exists = True
        if book_already_exists is False:
            new_book = {
                "name": name,
                "author": author
            }
            self.books.append(new_book)
            return new_book
        else:
            return False

    def delete_by_name(self, name):
        self.books = [book for book in self.books if book["name"] != name]
