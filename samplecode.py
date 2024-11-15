from datetime import datetime

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_issued = False

    def __str__(self):
        status = "Available" if not self.is_issued else "Issued"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"

class User:
    def __init__(self, name):
        self.name = name
        self.issued_books = []

    def issue_book(self, book):
        if len(self.issued_books) < 3:
            book.is_issued = True
            self.issued_books.append(book)
            print(f"{self.name} has issued '{book.title}'.")
        else:
            print(f"{self.name} cannot issue more than 3 books.")

    def return_book(self, book):
        if book in self.issued_books:
            book.is_issued = False
            self.issued_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}' issued.")

    def list_issued_books(self):
        if not self.issued_books:
            print(f"{self.name} has no books issued.")
        else:
            print(f"{self.name} has issued:")
            for book in self.issued_books:
                print(f" - {book.title}")

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        print(f"Book '{title}' added to the library.")

    def add_user(self, name):
        user = User(name)
        self.users.append(user)
        print(f"User '{name}' added to the library system.")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        print(f"Book '{title}' not found in the library.")
        return None

    def find_user(self, name):
        for user in self.users:
            if user.name.lower() == name.lower():
                return user
        print(f"User '{name}' not found in the system.")
        return None

    def issue_book_to_user(self, title, username):
        user = self.find_user(username)
        book = self.find_book(title)
        if user and book and not book.is_issued:
            user.issue_book(book)
        elif book and book.is_issued:
            print(f"The book '{title}' is currently issued to another user.")

    def return_book_from_user(self, title, username):
        user = self.find_user(username)
        book = self.find_book(title)
        if user and book:
            user.return_book(book)

    def list_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f" - {book}")

    def list_users(self):
        if not self.users:
            print("No users registered in the library system.")
        else:
            print("Registered users:")
            for user in self.users:
                print(f" - {user.name}")

# Sample usage of the Library system
library = Library()

# Adding books to the library
library.add_book("To Kill a Mockingbird", "Harper Lee", "978-0061120084")
library.add_book("1984", "George Orwell", "978-0451524935")
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")

# Adding users to the library
library.add_user("Alice")
library.add_user("Bob")

# Listing all books
library.list_books()

# Issuing a book to a user
library.issue_book_to_user("1984", "Alice")

# Trying to issue the same book to another user
library.issue_book_to_user("1984", "Bob")

# Listing issued books for a user
user = library.find_user("Alice")
if user:
    user.list_issued_books()

# Returning a book
library.return_book_from_user("1984", "Alice")

# Trying to return a book that isn’t issued
library.return_book_from_user("1984", "Bob")

# Listing all books again to see the changes in status
library.list_books()