# book_class.py

class Book:
    def __init__(self, title, author, year):
        # Constructor: initializes the book with title, author, and year
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        # Destructor: prints a message when the object is deleted
        print(f"Deleting {self.title}")
    
    def __str__(self):
        # String representation: returns a user-friendly string format
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        # Official representation: returns a string that can recreate the object
        return f"Book('{self.title}', '{self.author}', {self.year})"


# The following code is for testing purposes. You would run it in main.py.
