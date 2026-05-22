# . Design a LibraryMember class that:
# Tracks total active members.
# Each member has a name and books_borrowed count.
# Has a function to borrow books, with borrowing limit common to all.
# Allows updating borrowing limit globally.
# Has a static function to check if book title is valid (non-empty string, reasonable length).
# Demonstrate:
# 1.Borrowing books for multiple users.
# 2.Changing borrowing limits.
# 3.Validating book titles before borrowing.

class LibraryMember:
    total_members = 0
    borrow_limit = 3

    def __init__(self, name):
        self.name = name
        self.books_borrowed = 0
        LibraryMember.total_members += 1

    # instance method
    def borrow_book(self, title):

        if self.books_borrowed < LibraryMember.borrow_limit:
            self.books_borrowed += 1
            print(self.name, "borrowed", title)
        else:
            print(self.name, "has reached borrowing limit")

    # class method
    @classmethod
    def update_limit(cls, new_limit):
        cls.borrow_limit = new_limit
        print("Borrow limit updated to:", cls.borrow_limit)

    # static method
    @staticmethod
    def valid_title(title):
        return isinstance(title, str) and len(title) > 0 and len(title) <= 50
# 1. Creating members
m1 = LibraryMember("Harshita")
m2 = LibraryMember("Ravi")

# Borrowing books
m1.borrow_book("Python Basics")
m1.borrow_book("Data Science")

m2.borrow_book("AI")
m2.borrow_book("")   # invalid title

print("\nBooks Borrowed:")
print(m1.name, ":", m1.books_borrowed)
print(m2.name, ":", m2.books_borrowed)

# 2. Change borrowing limit
LibraryMember.update_limit(5)

# Borrow more books
m1.borrow_book("Machine Learning")
m1.borrow_book("Deep Learning")

# 3. Validation
print("\nTotal Active Members:", LibraryMember.total_members)
