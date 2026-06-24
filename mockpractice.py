# 1. Product and Cart
# Create a Product class with private __price and public name.
# Create a Cart class that stores products.
# Use:
# cart + product → add product
# cart - product → remove product
# len(cart) → number of products
# product in cart → check product exists
# str(cart) → display all products

class Product:
    def __init__(self,name,price):
        self.name = name
        self.__price = price
    @property
    def get_price(self):
        return self.__price
    def __repr__(self):
        return f"{self.name} , {self.__price}"
class Cart:
    def __init__(self):
        self.__products = []

    def __add__(self, other):
        self.__products.append(other)
        return self
    def __sub__(self, other):
        if other in self.__products:
            self.__products.remove(other)
            return self
        else:
            print("Product not found")
            return self
    def __len__(self):
        return len(self.__products)
    def __contains__(self, other):
        return other in self.__products
    def __repr__(self):
        return f"Products are:{self.__products}"

# p1=Product("Laptop" , 50000)
# p2=Product("Mouse" , 2000)
# print(p1)
# print(p2)
# c=Cart()
# c+p1
# c+p2
# print(c)
# print("total products are",len(c))
# print("Mouse of cart",p2 in c)
# c-p2
# print(c)


# Library and Books
# Create an abstract class LibraryItem with abstract method details().
# Create Book class inheriting from it.
# Create Library class.
# Use:
# library + book
# library - book
# len(library)
# book in library
# str(library)

from abc import ABC , abstractmethod
class LibraryItem(ABC):

    def details(self):
        pass

class Book(LibraryItem):
    def __init__(self, title):
        self.title = title

    def details(self):
        return f"Book: {self.title}"

    def __repr__(self):
        return self.title
class Library:
    def __init__(self):
        self.book=[]
    def __add__(self, other):
        self.book.append(other)
        return self
    def __sub__(self, other):
        if other in self.book:
            self.book.remove(other)
            return self
        else:
            print("Book not found")
            return self
    def __len__(self):
        return len(self.book)
    def __contains__(self, other):
        return other in self.book
    def __repr__(self):
        return f"{self.book}"
# b1 = Book("Python")
# b2 = Book("Java")
# library = Library()
# library + b1
# library + b2
# print(library)
# print("Total books:", len(library))
# print("Python book in library?", b1 in library)
# library - b1
# print("\nAfter removal:")
# print(library)


# 3. Employee Management
# Create Employee class with protected _salary.
# Create Manager and Developer classes inheriting Employee.
# Use:
# emp1 + emp2 → total salaries
# emp1 > emp2 → compare salaries
# str(employee) → employee details

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self._salary = salary
    def __add__(self, other):
        return self._salary + other._salary
    def __gt__(self, other):
        return self._salary > other._salary
    def __str__(self):
        return f"{self.name} , {self._salary}"
class Manager(Employee):
    def __init__(self,name, salary,department):
        super().__init__(name,salary)
        self.department = department
    def __str__(self):
        return f"{self.name} , {self._salary} , {self.department}"


class Developer(Employee):
    def __init__(self,name, salary,department,language):
        super().__init__(name,salary)
        self.department = department
        self.language = language

    def __str__(self):
        return f"{self.name} , {self._salary} , {self.department} , {self.language}"
# m1 = Manager("Ravi", 80000, "HR")
# d1 = Developer("Harshita", 60000,"Developer", "Python")
# print(m1)
# print(d1)
# print("Total Salary:", m1 + d1)
# print("Manager salary greater?", m1 > d1)

# Encapsulation Question
# Question 1: Bank Account Management System
# Create a class BankAccount that stores customer account details.
# Requirements:
# Store the account holder's name as a public variable.
# Store the account balance as a private variable.
# Provide methods:
# deposit(amount) to add money.
# withdraw(amount) to withdraw money.
# Withdrawal should not be allowed if the amount exceeds the available balance.
# Create a property called balance to view the current balance.
# Display account details after every transaction.

class BankAccount:
    def __init__(self,name,bal):
        self.name = name
        self.__bal = bal
    def deposit(self,amount):
        if amount>0:
            self.__bal=self.__bal+amount
            return self.__bal
        else:
            print("Amount should be positive")
    def withdraw(self,amount):
        if amount<self.__bal:
            self.__bal-=amount
            return self.__bal
        else:
            print("Balance becomes negative")
    @property
    def bal(self):
        return self.__bal
# b1=BankAccount("Harshita",2000)
# print(b1.bal)
# b1.deposit(2000)
# print(b1.bal)
# b1.withdraw(2000)
# print(b1.bal)

# Abstraction Question
# Question 2: Online Payment System
# Design an abstract class PaymentMethod.
# Requirements:
# The abstract class must contain an abstract method pay(amount).
# Create the following subclasses:
# CreditCard
# UPI
# Wallet
# Each subclass must provide its own implementation of the pay() method.
# Create objects of all payment methods and demonstrate payment processing.
# Display the payment method used and the amount paid.

from abc import ABC , abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class CreditCard(PaymentMethod):
    def pay(self,amount):
        print(f"Paid {amount} using creditcard")
class Upi(PaymentMethod):
    def pay(self,amount):
        print(f"Paid {amount} using upi")
class Wallet(PaymentMethod):
    def pay(self,amount):
        print(f"Paid {amount} using wallet")
cc=CreditCard()
cc.pay(2000)
u=Upi()
u.pay(2000)
w=Wallet()
w.pay(2000)