class Book:
    """Represents a book in the library."""
    
    def __init__(self, title, author):
        """Initialize the book with title, author, and set it as available (not checked out)."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute, False means available
    
    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Return the book, marking it as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Return whether the book is available or checked out."""
        return not self._is_checked_out
    
    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"

class Library:
    """Represents the library and manages a collection of books."""
    
    def __init__(self):
        """Initialize the library with an empty book collection."""
        self._books = []
    
    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out: {book}")
                    return True
                else:
                    print(f"The book '{title}' is already checked out.")
                    return False
        print(f"The book '{title}' is not in the library.")
        return False
    
    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned: {book}")
                    return True
                else:
                    print(f"The book '{title}' was not checked out.")
                    return False
        print(f"The book '{title}' is not in the library.")
        return False
    
    def list_available_books(self):
        """List all books that are available (not checked out)."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books.")
