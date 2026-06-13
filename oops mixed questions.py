#2.Create a ShoppingCart class where:
# • items are stored privately
# • users cannot directly modify item list
# • only add/remove methods are allowed
# • provide a method to get a safe copy of the cart items (not direct reference to internal list)

class ShoppingCart:
    def __init__(self):
        self.__items=[]
    def add_item(self,item):
        return self.__items.append(item)
    def remove_item(self,item):
        if item in self.__items:
            return self.__items.remove(item)
    @property
    def get_items(self):
        return self.__items.copy()
# s=ShoppingCart()
# s.add_item("Laptop")
# s.add_item("Mouse")
# print(s.get_items)
# s.remove_item("Mouse")
# print(s.get_items)


#3.Create a BankAccount class that stores:
# • account number
# • balance (should not be directly modifiable)
# You must:
# Make the balance attribute inaccessible from outside.
# Provide functions to deposit/withdraw that validate the amount.
# Prevent withdrawal if balance becomes negative.
# Show what happens if someone tries to modify balance directly and why
# encapsulation prevents it.

class BankAccount:
    def __init__(self,accno,balance):
        self.accno=accno
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            return self.__balance
        else:
            print("Amount must be positive")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            return self.__balance
    def get_balance(self):
        return self.__balance
# acc=BankAccount(101,5000)
# print("Initial balance:",acc.get_balance())
# acc.deposit(1000)
# print(acc.get_balance())
# acc.withdraw(2000)
# print(acc.get_balance())
# acc.__balance=10000
# print("Directly Modified Balance:", acc.__balance)
# print("Actual Balance:", acc.get_balance())

# 4.Create a Vector class that supports:
# + operator → add coordinates
# == operator → compare equality
# Show how operator overloading gives natural polymorphism to user-defined classes.

class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self, other):
        return self.a+other.a , self.b+ other.b
    def __eq__(self, other):
        return self.a == other.a , self.b == other.b
    def __str__(self):
        return f"A:{self.a}, B:{self.b}"
# v1=Vector(10,20)
# print(v1)
# v2=Vector(40,50)
# print(v2)
# print(v1+v2)
# print(v1==v2)

#5.	Create:
# •	Abstract class PaymentMethod with pay(), validate()
# •	Subclasses: CardPayment, WalletPayment, UPIPayment
# •	Encapsulate user balance
# •	Use @property to control reading available funds
# •	Overload + operator to combine two payment methods into “split payment”
# •	Demonstrate polymorphism through a checkout loop.

from abc import ABC , abstractmethod
class PaymentMethod(ABC):
    def __init__(self,b):
        self.__b=b
    @abstractmethod
    def pay(self):
        pass
    @abstractmethod
    def validate(self):
        pass
    @property
    def bal(self):
        return self.__b
    @bal.setter
    def bal(self,nb):
        self.__b=nb
    def __add__(self, other):
        return self.pay()+other.pay() // 2
class CardPayment(PaymentMethod):
    def pay(self):
        return 500
    def validate(self,amount):
        return amount>=0
class WalletPayment(PaymentMethod):
    def pay(self):
        return 10
    def validate(self,amount):
        return amount>=0
class UPIPayment(PaymentMethod):
    def pay(self):
        return 100
    def validate(self,amount):
        return amount>=0
# def checkout(l):
#     print("1. Card")
#     print("2. Wallet")
#     print("3. UPI")
#
#     choice = int(input("Choose payment method: "))
#     amount = int(input("Enter amount: "))
#
#     payment = l[choice - 1]
#
#     if payment.validate(amount):
#         print(f"Payment Successful using {choice}")
#     else:
#         print("Payment Failed")
#
# payments = [
#     CardPayment(1000),
#     WalletPayment(500),
#     UPIPayment(50)
# ]
#
# checkout(payments)

#5.Design a banking system with:
# An abstract base class Account with deposit(), withdraw(), calculate_interest().
# Subclasses: SavingsAccount, CurrentAccount, FixedDepositAccount.
# Each account must:
# oEncapsulate balance (private)
# oProvide controlled access through properties
# oOverride interest calculation differently
# Include a static method to validate amount.
# Include a class method to update bank-wide interest policies.

from abc import ABC, abstractmethod

class Account(ABC):
    bank_interest_rate = 5  # default bank policy

    def __init__(self, balance):
        self.__balance = balance

    # Property for controlled access
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")

    # Static method
    @staticmethod
    def validate_amount(amount):
        return amount > 0

    def deposit(self, amount):
        if Account.validate_amount(amount):
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if Account.validate_amount(amount) and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance or invalid amount")

    @abstractmethod
    def calculate_interest(self):
        pass

    # Class method
    @classmethod
    def update_interest_policy(cls, rate):
        cls.bank_interest_rate = rate
        print(f"Bank interest policy updated to {rate}%")


class SavingsAccount(Account):
    def calculate_interest(self):
        return self.balance * 0.04


class CurrentAccount(Account):
    def calculate_interest(self):
        return self.balance * 0.01


class FixedDepositAccount(Account):
    def calculate_interest(self):
        return self.balance * 0.07


# Driver Code
s = SavingsAccount(10000)
c = CurrentAccount(10000)
f = FixedDepositAccount(10000)

s.deposit(2000)
s.withdraw(1000)

print("Savings Balance:", s.balance)
print("Savings Interest:", s.calculate_interest())

print("Current Interest:", c.calculate_interest())
print("FD Interest:", f.calculate_interest())

Account.update_interest_policy(6)






