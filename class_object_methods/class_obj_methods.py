#


# Create a class Student with instance attributes name and marks.
# Add an instance method is_passed() that returns True if marks > 40.
# Then create 2 student objects and print whether each has passed or failed.
#
# class Student:
#     def __init__ (self,name,marks):
#         self.name=name
#         self.marks=marks
#     def is_passed(self):
#         if (self.marks>40):
#             return True
#
# s1=Student("Harshita",50)
# s2=Student("Sweety",30)
# for s in [s1,s2]:
#     if s.is_passed():
#         print(f"{s.name} has passed")
#     else:
#         print(f"{s.name} has failed")
#
#
# Create a class Employee with attributes name and company_name = "TechCorp".
# Add a class method change_company(cls, new_name) to update the company name for all employees.
# Demonstrate how this change affects all instances.
#
# class Employee:
#     company_name="TechCorp"
#     def __init__(self,name):
#         self.name=name
#     @classmethod
#     def change_company(cls,new_name):
#         cls.company_name=new_name
# e1=Employee("Harshita")
# print(e1.company_name,e1.name)
# Employee.change_company("CVCORP")
# print(e1.name,e1.company_name)
#
#
# Create a class MathOps with a static method is_even(num) that returns True if the number is even.
# Then call it both from the class and an instance.
#
# class MathOps:
#     @staticmethod
#     def is_even(num):
#         return(num%2==0)
# print(MathOps.is_even(10))
# print(MathOps.is_even(5))
# obj=MathOps()
# print(obj.is_even(12))
# print(obj.is_even(15))
#
#
# Create a class Car with:
# instance attribute mileage
# class attribute wheels = 4
# Add an instance method display_specs() that prints mileage and wheels.
# Then change wheels using a class method, and print again.
#
# class Car:
#     wheels=4
#     def __index__(self,mileage):
#         self.mileage=mileage
#     def display_specs(self):
#         print(f"Mileage{self.mileage},Wheels{Car.wheels}")
#     @classmethod
#     def change_wheels(cls,new_wheels):
#         cls.wheels=new_wheels
# c1 = Car(10)
# c2 = Car(20)
# print("Before change:")
# c1.display_specs()
# c2.display_specs()
# print("After change:")
# Car.change_wheels(6)
# c1.display_specs()
# c2.display_specs()
#
#
# Create a class Temperature with:
# instance attribute celsius
# a static method to_fahrenheit(celsius)
# an instance method show_conversion() that uses the static method to print both values.
#
# class Temperature:
#     def __init__(self,celcius):
#         self.celcius=celcius
#     @staticmethod
#     def to_fahrenheit(celcius):
#         return (celcius*9/5)+32
#
#     def show_conversion(self):
#         print("celcius",self.celcius)
#         f=Temperature.to_fahrenheit(self.celcius)
#         print("fahrenheit",f)
#
#
# obj=Temperature(32)
# obj.show_conversion()

#
#
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





#
# Create a class Employee with:
# instance attributes: name, base_salary
# class variable: bonus_rate = 0.1
# instance method: final_salary() → base_salary + (base_salary × bonus_rate)
# class method: update_bonus(cls, new_rate) → updates bonus for all employees
# static method: is_valid_salary(sal) → checks if salary > 0
# Create two employees, show final salaries, update bonus rate, and show again.
#
class Employee:
    bonus_rate=0.1
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def final_salary(self):
        return self.base_salary+(self.base_salary*Employee.bonus_rate)
    @classmethod
    def update_bonus(cls,new_rate):
        cls.bonus_rate=new_rate
    @staticmethod
    def is_valid_salary(salary):
        return salary>0
e1=Employee("Harshita",10000)
e2=Employee("Sweety",20000)
print(e1.final_salary())
print(e2.final_salary())
Employee.update_bonus(2)
print(e1.final_salary())
print(e2.final_salary())
#

# Q8. Create a class Course with:
# class variable total_students
# instance variable student_name
# instance method enroll() → increments total_students
# class method show_total(cls) → prints total students
# static method is_eligible(age) → returns True if age ≥ 18
# Demonstrate enrolling multiple students and show total count.
# class Course:
#     total_students=0
#     def __init__(self,student_name):
#         self.student_name=student_name
#     def enroll(self):
#         Course.total_students+=1
#         print(f"{self.total_students} enrolled successfully")
#
#     @classmethod
#     def show_total(cls):
#         return cls.total_students
#     @staticmethod
#     def is_eligible(age):
#         return age>18
# s1=Course("Harshita")
# s2=Course("Sweety")
# s1.enroll()
# s2.enroll()
# Course.show_total()
# print(Course.is_eligible(17))
# print(Course.is_eligible(20))

# . Create a class BankAccount with:
# class variable bank_name
# instance variables holder and balance
# instance method deposit(amount)
# class method change_bank_name(cls, new_name)
# static method validate_amount(amount) → returns True if amount > 0
# Show transactions and how static + class methods work together.

class BankAccount:

    # Class variable
    bank_name = "State Bank"

    # Constructor
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    # Static method
    @staticmethod
    def validate_amount(amount):
        return amount > 0

    # Instance method
    def deposit(self, amount):

        # Using static method inside instance method
        if BankAccount.validate_amount(amount):
            self.balance += amount
            print(f"{amount} deposited successfully")
        else:
            print("Invalid deposit amount")

    # Class method
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
        print(f"\nBank name changed to: {cls.bank_name}")

    # Display method
    def display(self):
        print("\nAccount Details")
        print("Bank Name :", BankAccount.bank_name)
        print("Holder Name :", self.holder)
        print("Balance :", self.balance)


# ---------------- DEMONSTRATION ----------------

# Creating objects
# acc1 = BankAccount("Harshita", 5000)
# acc2 = BankAccount("Rahul", 3000)
#
# # Display initial details
# acc1.display()
# acc2.display()
#
# # Transactions
# acc1.deposit(2000)
# acc2.deposit(-500)
#
# # Display updated balances
# acc1.display()
# acc2.display()
#
# # Changing bank name using class method
# BankAccount.change_bank_name("National Bank")
#
# # Updated bank name reflected in all objects
# acc1.display()
# acc2.display()
# #
#  Create a class Student with:
# class variable passing_marks = 40
# instance attributes name, marks
# instance method result() → prints pass/fail using class variable
# class method update_passing_marks(cls, new_marks)
# static method grade_category(marks) → returns "A", "B", "C" based on score ranges
# Use all three in a program that:
# 1.Creates students
# 2.Updates the passing criteria
# Displays grade category and result

# class Student:
#     passing_marks=40
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def result(self):
#         if self.marks>=Student.passing_marks:
#             print("pass")
#         else:
#             print("fail")
#     @classmethod
#     def update_passing_marks(cls,new_marks):
#         cls.passing_marks=new_marks
#     @staticmethod
#     def grade_category(marks):
#         if marks>=75:
#             return "A"
#         elif( marks>=50):
#             return "B"
#         else:
#             return "C"
# s1 = Student("Harshita", 82)
# s2 = Student("Sweety", 55)
# s3 = Student("Ravi", 38)
# print("Before updating")
# for s in [s1,s2,s3]:
#     print(f"{s.name} Grade: {Student.grade_category(s.marks)}")
#     s.result()
# Student.update_passing_marks(45)
# print("After updating")
# for s in [s1,s2,s3]:
#     print(f"{s.name} Grade: {Student.grade_category(s.marks)}")
#     s.result()
