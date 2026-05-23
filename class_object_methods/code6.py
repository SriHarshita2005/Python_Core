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
    total_books=0
    def __init__(self,title,author):
        if Book.is_valid_title(title):
            self.title=title
            self.author=author
            Book.total_books+=1

    @classmethod
    def from_string(cls,book_str):
        t,a=book_str.split("-")
        return cls(t,a)
    @staticmethod
    def is_valid_title(title):
        return len(title) >= 3
b1=Book("ABC","Ha")
print(b1.title , b1.author)
Book.from_string("abc-xyz")
print(Book.total_books)




