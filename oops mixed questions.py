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
v1=Vector(10,20)
print(v1)
v2=Vector(40,50)
print(v2)
print(v1+v2)
print(v1==v2)



