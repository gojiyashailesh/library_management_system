import pytest
from unittest.mock import MagicMock, patch
from src.app import LibraryApp

@pytest.fixture
def library_app():
    app = LibraryApp()
    app.library = MagicMock()
    return app

def test_add_book(library_app, monkeypatch):
    inputs = iter(['9780261102217', 'The Lord of the Rings', 'J.R.R. Tolkien', '1954'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    with patch('builtins.print') as mock_print:
        library_app.add_book()
    
    library_app.library.add_book.assert_called_once_with('9780261102217', 'The Lord of the Rings', 'J.R.R. Tolkien', 1954)
    mock_print.assert_called_with("Book 'The Lord of the Rings' added successfully.")

def test_borrow_book(library_app, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '9780261102217')
    
    with patch('builtins.print') as mock_print:
        library_app.borrow_book()
    
    library_app.library.borrow_book.assert_called_once_with('9780261102217')
    mock_print.assert_called_with("Book borrowed successfully.")

def test_return_book(library_app, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '9780261102217')
    
    with patch('builtins.print') as mock_print:
        library_app.return_book()
    
    library_app.library.return_book.assert_called_once_with('9780261102217')
    mock_print.assert_called_with("Book returned successfully.")

def test_view_available_books_empty(library_app):
    library_app.library.view_available_books.return_value = []
    
    with patch('builtins.print') as mock_print:
        library_app.view_available_books()
    
    mock_print.assert_called_with("No books are currently available.")

def test_view_available_books_not_empty(library_app):
    mock_book = MagicMock()
    mock_book.isbn = '9780261102217'
    mock_book.title = 'The Lord of the Rings'
    mock_book.author = 'J.R.R. Tolkien'
    mock_book.publication_year = 1954
    library_app.library.view_available_books.return_value = [mock_book]
    
    with patch('builtins.print') as mock_print:
        library_app.view_available_books()
    
    mock_print.assert_called()

def test_run_exit(library_app, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')
    
    with patch('builtins.print') as mock_print:
        library_app.run()
    
    mock_print.assert_called_with("Thank you for using the Library Management System. Goodbye!")

def test_run_invalid_choice(library_app, monkeypatch):
    inputs = iter(['6', '5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    with patch('builtins.print') as mock_print:
        library_app.run()
    
    mock_print.assert_any_call("Invalid choice. Please try again.")