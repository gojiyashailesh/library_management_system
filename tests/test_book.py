import pytest
from src.book import Book

def test_book_creation():
    book_obj = Book("9780132350884", "Clean Code", "Robert C. Martin", 2008)
    assert book_obj.isbn == "9780132350884"
    assert book_obj.title == "Clean Code"
    assert book_obj.author == "Robert C. Martin"
    assert book_obj.publication_year == 2008
    assert not book_obj.is_borrowed

def test_book_invalid_isbn():
    with pytest.raises(ValueError):
        Book("123", "Clean Code", "Robert C. Martin", 2008)
