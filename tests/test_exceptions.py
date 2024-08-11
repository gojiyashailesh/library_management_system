import pytest
from src.library import Library
from src.exceptions import BookNotFoundException, BookNotBorrowedException, BookAlreadyExistsException

def test_return_nonexistent_book():
    library = Library()
    with pytest.raises(BookNotFoundException):
        library.return_book("9789876543210")

def test_return_not_borrowed_book():
    library = Library()
    library.add_book("9780123456789", "Test Book", "Test Author", 2021)
    with pytest.raises(BookNotBorrowedException):
        library.return_book("9780123456789")

def test_add_existing_book():
    library = Library()
    library.add_book("9780123456789", "Test Book", "Test Author", 2021)
    with pytest.raises(BookAlreadyExistsException):
        library.add_book("9780123456789", "Test Book", "Test Author", 2021)
