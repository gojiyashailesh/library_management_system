from .book import Book
from .exceptions import BookAlreadyExistsException
from .exceptions import BookNotFoundException, BookAlreadyBorrowedException,BookNotBorrowedException

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, isbn: str, title: str, author: str, publication_year: int):
        if any(book.isbn == isbn for book in self.books):
            raise BookAlreadyExistsException(f"A book with ISBN {isbn} already exists in the library.")
        book = Book(isbn, title, author, publication_year)
        self.books.append(book)
        
    def borrow_book(self, isbn: str):
        book = self._find_book_by_isbn( isbn)
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"The book '{book.title}' is already borrowed.")
        book.is_borrowed = True

    def _find_book_by_isbn(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                return book
        raise BookNotFoundException(f"No book found with ISBN: {isbn}")
    
    def return_book(self, isbn: str):
        book = self._find_book_by_isbn(isbn)
        if not book.is_borrowed:
            raise BookNotBorrowedException(f"The book '{book.title}' has not been borrowed.")
        book.is_borrowed = False
        
    def view_available_books(self):
        return [book for book in self.books if not book.is_borrowed]
        