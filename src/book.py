import re

class Book:
    def __init__(self, isbn: str, title: str, author: str, publication_year: int):
        try:
            self.isbn = self.validate_isbn(isbn)
        except ValueError as e:
            raise ValueError(f"Invalid ISBN: {e}")
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_borrowed = False
    
    @staticmethod
    def validate_isbn(isbn: str) -> str:
        isbn = re.sub(r'[-\s]', '', isbn)
        if not re.match(r'^\d{13}$', isbn):
            raise ValueError("ISBN must be a 13-digit number.")
        return isbn