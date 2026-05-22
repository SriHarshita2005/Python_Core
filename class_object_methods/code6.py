# Create a class Book with:
# instance attributes title, author
# a class variable total_books
# a class method from_string(cls, book_str) that creates an object from "title-author" format
# a static method is_valid_title(title) that checks if title has at least 3 characters
# increment total_books for every book created
# Demonstrate:
# Creating books using both the constructor and the class method
# Validating titles before creation

class Book:

    # Class variable
    total_books = 0

    # Constructor
    def __init__(self, title, author):

        # Validate title before creating object
        if Book.is_valid_title(title):
            self.title = title
            self.author = author

            # Increment total books
            Book.total_books += 1

            print(f"Book '{self.title}' created successfully")

        else:
            print("Invalid title! Title must contain at least 3 characters.")

    # Class method
    @classmethod
    def from_string(cls, book_str):

        # Split string into title and author
        title, author = book_str.split("-")

        # Create object using constructor
        return cls(title, author)

    # Static method
    @staticmethod
    def is_valid_title(title):
        return len(title) >= 3

    # Display method
    def display(self):
        print("\nBook Details")
        print("Title :", self.title)
        print("Author :", self.author)


# ---------------- DEMONSTRATION ----------------

# Creating books using constructor
b1 = Book("Python", "Guido")
b2 = Book("AI", "John")      # Invalid title

# Creating books using class method
b3 = Book.from_string("Django-Adrian")
b4 = Book.from_string("ML-Rahul")   # Invalid title

# Display valid books
if hasattr(b1, 'title'):
    b1.display()

if hasattr(b3, 'title'):
    b3.display()

# Total books created
print("\nTotal Books Created :", Book.total_books)
#


