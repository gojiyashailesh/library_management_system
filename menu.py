from src.library import Library

def print_menu():
    print("\n╔═══════════════════════════════╗")
    print("║   Library Management System   ║")
    print("╠═══════════════════════════════╣")
    print("║ 1. Add Book                   ║")
    print("║ 2. Borrow Book                ║")
    print("║ 3. Return Book                ║")
    print("║ 4. View Available Books       ║")
    print("║ 5. Exit                       ║")
    print("╚═══════════════════════════════╝")

def print_table(books):
    if not books:
        print("No books available.")
        return

    # Find the maximum width for each column
    isbn_width = max(len("ISBN"), max(len(book.isbn) for book in books))
    title_width = max(len("Title"), max(len(book.title) for book in books))
    author_width = max(len("Author"), max(len(book.author) for book in books))
    year_width = max(len("Year"), max(len(str(book.publication_year)) for book in books))

    # Print table header
    print("╔" + "═" * (isbn_width + 2) + "╦" + "═" * (title_width + 2) + "╦" + "═" * (author_width + 2) + "╦" + "═" * (year_width + 2) + "╗")
    print(f"║ {'ISBN':<{isbn_width}} ║ {'Title':<{title_width}} ║ {'Author':<{author_width}} ║ {'Year':<{year_width}} ║")
    print("╠" + "═" * (isbn_width + 2) + "╬" + "═" * (title_width + 2) + "╬" + "═" * (author_width + 2) + "╬" + "═" * (year_width + 2) + "╣")

    # Print table rows
    for book in books:
        print(f"║ {book.isbn:<{isbn_width}} ║ {book.title:<{title_width}} ║ {book.author:<{author_width}} ║ {book.publication_year:<{year_width}} ║")

    # Print table footer
    print("╚" + "═" * (isbn_width + 2) + "╩" + "═" * (title_width + 2) + "╩" + "═" * (author_width + 2) + "╩" + "═" * (year_width + 2) + "╝")

def main():
    library = Library()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            isbn = input("Enter ISBN: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            year = input("Enter Publication Year: ")
            try:
                year = int(year)
                library.add_book(isbn, title, author, year)
                print(f"Book '{title}' added successfully.")
            except ValueError:
                print("Invalid year. Please enter a valid integer for the publication year.")
            except BookAlreadyExistsException as e:
                print(f"Error: {e}")

        elif choice == '2':
            isbn = input("Enter ISBN of the book to borrow: ")
            try:
                library.borrow_book(isbn)
                print("Book borrowed successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '3':
            isbn = input("Enter ISBN of the book to return: ")
            try:
                library.return_book(isbn)
                print("Book returned successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '4':
            available_books = library.view_available_books()
            if available_books:
                print("\nAvailable Books:")
                print_table(available_books)
            else:
                print("No books available.")

        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()