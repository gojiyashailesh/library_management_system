from .library import Library
from prettytable import PrettyTable

class LibraryApp:
    def __init__(self):
        self.library = Library()

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                self.return_book()
            elif choice == '4':
                self.view_available_books()
            elif choice == '5':
                print("Thank you for using the Library Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def display_menu(self):
        menu = PrettyTable()
        menu.field_names = ["Option", "Action"]
        menu.align["Option"] = "l"
        menu.align["Action"] = "l"
        menu.add_rows([
            ["1", "Add Book"],
            ["2", "Borrow Book"],
            ["3", "Return Book"],
            ["4", "View Available Books"],
            ["5", "Exit"]
        ])
        print("\nLibrary Management System")
        print(menu)

    def add_book(self):
        isbn = input("Enter ISBN (13 digits): ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        year = input("Enter Publication Year: ")
        try:
            self.library.add_book(isbn, title, author, int(year))
            print(f"Book '{title}' added successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def borrow_book(self):
        isbn = input("Enter ISBN of the book to borrow: ")
        try:
            self.library.borrow_book(isbn)
            print("Book borrowed successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def return_book(self):
        isbn = input("Enter ISBN of the book to return: ")
        try:
            self.library.return_book(isbn)
            print("Book returned successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def view_available_books(self):
        available_books = self.library.view_available_books()
        if not available_books:
            print("No books are currently available.")
        else:
            table = PrettyTable()
            table.field_names = ["ISBN", "Title", "Author", "Year"]
            for book in available_books:
                table.add_row([book.isbn, book.title, book.author, book.publication_year])
            print(table)

if __name__ == "__main__":
    app = LibraryApp()
    app.run()