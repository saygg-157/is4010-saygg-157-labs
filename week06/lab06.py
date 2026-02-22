"""
Lab 06: Object-Oriented Programming
Demonstrates class creation, inheritance, and method overriding.
"""


class Book:
    """Represents a physical book with title, author, and publication year."""
    
    def __init__(self, title, author, year):
        """
        Initialize a Book object.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        """Return a user-friendly string representation of the book."""
        return f'Title: "{self.title}" | Author: {self.author} | Year: {self.year}'
    
    def get_age(self):
        """
        Calculate the age of the book based on publication year.
        
        Returns:
            int: The age of the book (current year 2025 - publication year)
        """
        return 2025 - self.year


class EBook(Book):
    """Represents a digital book that inherits from Book and adds file size."""
    
    def __init__(self, title, author, year, file_size):
        """
        Initialize an EBook object.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year
            file_size (int): The file size in megabytes (MB)
        """
        super().__init__(title, author, year)
        self.file_size = file_size
    
    def __str__(self):
        """Return a string representation including file size."""
        parent_str = super().__str__()
        return f"{parent_str} | File Size: {self.file_size} MB"


if __name__ == '__main__':
    print("\n" + "=" * 70)
    print(" " * 18 + "LIBRARY MANAGEMENT SYSTEM")
    print(" " * 25 + "BOOK CATALOG")
    print("=" * 70)
    
    # Test the Book class
    print("\nPHYSICAL BOOK")
    print("-" * 70)
    book1 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    print(f"  {book1}")
    print(f"  Age: {book1.get_age()} years old")
    print("-" * 70)
    
    # Test the EBook class
    print("\nDIGITAL BOOK (EBOOK)")
    print("-" * 70)
    ebook1 = EBook("Dune", "Frank Herbert", 1965, 5)
    print(f"  {ebook1}")
    print(f"  Age: {ebook1.get_age()} years old")
    print("-" * 70)
    
    print("=" * 70 + "\n")
