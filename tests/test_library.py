import pytest
from src.library_management.library import Library
from src.library_management.exceptions import BookNotFoundException, BookAlreadyBorrowedException

def test_add_book():
    library = Library()
    library.add_book("9780132350884", "Clean Code", "Robert C. Martin", 2008)
    assert len(library.books) == 1
    assert library.books[0].title == "Clean Code"
    
def test_borrow_book():
    library = Library()
    library.add_book("9780132350884", "Clean Code", "Robert C. Martin", 2008)
    library.borrow_book("9780132350884")
    assert library.books[0].is_borrowed

def test_borrow_nonexistent_book():
    library = Library()
    with pytest.raises(BookNotFoundException):
        library.borrow_book("9789876543210")  # Example ISBN of a book not added

def test_borrow_already_borrowed_book():
    library = Library()
    library.add_book("9780132350884", "Clean Code", "Robert C. Martin", 2008)
    library.borrow_book("9780132350884")
    with pytest.raises(BookAlreadyBorrowedException):
        library.borrow_book("9780132350884")
        
def test_return_book():
    library = Library()
    library.add_book("9780132350884", "Clean Code", "Robert C. Martin", 2008)
    library.borrow_book("9780132350884")
    library.return_book("9780132350884")
    assert not library.books[0].is_borrowed

def test_view_available_books():
    library = Library()
    library.add_book("9780132350884", "Clean Code", "Robert C. Martin", 2008)
    library.add_book("9780134757599", "Refactoring", "Martin Fowler", 2018)
    library.borrow_book("9780132350884")
    available_books = library.view_available_books()
    assert len(available_books) == 1
    assert available_books[0].title == "Refactoring"

