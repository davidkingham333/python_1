class Book:
    def __init__(self, name, author, pub_year,):
        self.name = name
        self.author = author
        self.pub_year = pub_year
        self.book_borrowed = False

    def borrow(self):
        if not self.book_borrowed:
            self.book_borrowed = True
            print(f"The book '{self.name}' has been borrowed.")
        else:
            print(f"The book '{self.name}' is already borrowed.")

    def return_the_book(self):
        if self.book_borrowed:
            self.book_borrowed = False
            print(f"The book '{self.name}' has been returned.")
        else:
            print(f"The book '{self.name}' was not borrowed.")

class Library:
    def __init__(self):
        self.books = []

    def add_a_book(self, book):
        self.books.append(book)

    def print_books(self):
        print("List of books:")
        for book in self.books:
            state = "borrowed" if book.book_borrowed else "available"
            print(f" - '{book.name}' by {book.author} ({book.pub_year}): {state}")
        
    def borrow_book(self, name):
        for book in self.books:
            if book.name == name:
                book.borrow()
                return
        print(f"The book '{name}' is not available in the library.")
            
    def return_book(self, name):
        for book in self.books:
            if book.name == name:
                book.return_the_book()
                return
        print(f"The book '{name}' is not available in the library.")


library = Library()

book1 = Book("1984", "George Orwell", 1949)
book2 = Book("Beyond Good and Evil", "Friedrich Nietzsche", 1886)

library.add_a_book(book1)
library.add_a_book(book2)

library.print_books()

library.borrow_book("1984")
library.print_books()

library.return_book("1984")
library.print_books()