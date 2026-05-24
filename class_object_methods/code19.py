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

    def borrow_book(self, title):
        if not LibraryMember.check_title(title):
            print("Invalid book title")
            return

        if self.books_borrowed < LibraryMember.borrow_limit:
            self.books_borrowed += 1
            print(self.name, "borrowed", title)
        else:
            print(self.name, "reached borrow limit")

    @classmethod
    def update_limit(cls, new_limit):
        cls.borrow_limit = new_limit

    @staticmethod
    def check_title(title):
        return isinstance(title, str) and len(title.strip()) > 0 and len(title) <= 30


# Creating members
m1 = LibraryMember("Harshita")
m2 = LibraryMember("Ravi")

# Borrowing books
m1.borrow_book("Python Basics")
m1.borrow_book("AI Book")

m2.borrow_book("Data Science")
m2.borrow_book("Machine Learning")
m2.borrow_book("DBMS")
m2.borrow_book("Networks")   # limit reached

# Changing borrowing limit
LibraryMember.update_limit(5)

print("New Borrow Limit:", LibraryMember.borrow_limit)

# Borrow again after limit change
m2.borrow_book("Networks")

# Checking invalid titles
m1.borrow_book("")
m1.borrow_book(" ")

# Total members
print("Total Members:", LibraryMember.total_members)



