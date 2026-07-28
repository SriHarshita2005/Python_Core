# Q1. Create a class Animal with make_sound() and derived classes Dog, Cat, Cow that
# override it.
# Demonstrate polymorphism by iterating over a list of different animal objects and calling
# make_sound().

class Animal:
    def make_sound(self):
        print("Animals make sound")
class Dog(Animal):
    def make_sound(self):
        print("Bow Bow")
class Cat(Animal):
    def make_sound(self):
        print("Mew Mew")
class Cow(Animal):
    def make_sound(self):
        print("Moo Moo")
# l=[Dog() , Cat() , Cow()]
# for i in l:
#     i.make_sound()

# Q2. Write a function operate(device) that calls device.start().
# Pass in objects of Car, Computer, and WashingMachine — all of which define a start()
# method, but share no inheritance relationship.
# Show that Python’s polymorphism works through behavior, not type.

class Car:
    def start(self):
        print("Car starting")
class Computer:
    def start(self):
        print("Computer starting")
class WashingMachine:
    def start(self):
        print("Washing machine starting")
def operate(device):
    device.start()
# operate(Car())
# operate(Computer())
# operate(WashingMachine())

# Q3. Create a Vector class that supports:
# • + operator → add coordinates
# • == operator → compare equality
# Show how operator overloading gives natural polymorphism to user-defined classes.

class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self, other):
        return self.a+other.a , self.b+other.b
    def __eq__(self, other):
        return self.a == other.a , self.b == other.b
    def __str__(self):
        return f"A:{self.a} , B:{self.b}"
# v1=Vector(10,20)
# v2=Vector(20,30)
# print(v1)
# print(v2)
# print(v1+v2)
# print(v1==v2)

# Q4. Create a base class Transport with move() and derived classes Bus and Bike that
# override it but also call the parent implementation using super().
# Show the combination of reuse + custom behavior.

class Transport:
    def move(self):
        print("Transport is moving")
class Bus(Transport):
    def move(self):
        print("Bus is moving")
        super().move()
class Bike(Transport):
    def move(self):
        print("Bike is moving")
        super().move()
# Bus().move()
# Bike().move()

# Q5. Using the abc module, create an abstract class Notification with send().
# Implement subclasses EmailNotification, SMSNotification, PushNotification — each
# with its own send() logic.
# Demonstrate polymorphism by looping over all and calling send().

from abc import ABC , abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass
class EmailNotification(Notification):
    def send(self):
        print("Email Sent")
class SMSNotification(Notification):
    def send(self):
        print("SMS Sent")
class PushNotification(Notification):
    def send(self):
        print("Push Notification Sent")
# notification = [EmailNotification() , SMSNotification() , PushNotification()]
# for n in notification:
#     n.send()

# Q6. Design:
# • Base class Payment with process(amount)
# • Subclass CreditCardPayment adds process(amount, card_type)
# Demonstrate what happens when overriding with different signatures and how Python
# handles it.

class Payment:
    def process(self,amount):
        print("Processing",amount)
class CreditCardPayment(Payment):
    def process(self,amount,card_type):
        print("Processing",amount, "through",card_type)
# c=CreditCardPayment()
# c.process(1000,"VISA")

# Q7. Create:
# • Class Sorter with change(strategy) method. Separate strategy classes: BS, MS, QS,
# each implementing a different logic method.
# Demonstrate how polymorphism can be achieved without inheritance by using
# interchangeable strategy objects.

class BS:
    def logic(self):
        print("Bubble sort")
class MS:
    def logic(self):
        print("Merge sort")
class QS:
    def logic(self):
        print("Quick Sort")
class Sorter:
    def change(self,strategy):
        self.strategy = strategy
    def sort(self):
        self.strategy.logic()
# s=Sorter()
# l = [BS(), MS(), QS()]
#
# for i in l:
#     s.change(i)
#     s.sort()

# . Create:
# • Base Account → withdraw()
# • Subclass SavingsAccount → modifies withdraw()
# • Subclass PremiumSavingsAccount → overrides again but calls parent using super()
# Show how polymorphism works across multiple levels.

class Account:
    def withdraw(self, amount):
        print("Withdraw:", amount)

class SavingsAccount(Account):
    def withdraw(self, amount):
        print("Savings Withdrawal:", amount)

class PremiumSavingsAccount(SavingsAccount):
    def withdraw(self, amount):
        super().withdraw(amount)
        print("Premium Benefits Applied")

# obj = PremiumSavingsAccount()
# obj.withdraw(5000)

# Q9. Create a function draw(shape) that works for objects of classes Circle, Square, and
# Rectangle,
# each implementing a draw() method.
# Add another unrelated class Car with draw() and pass it — what happens and why?

class Circle:
    def draw(self):
        print("Drawing Circle")


class Square:
    def draw(self):
        print("Drawing Square")


class Rectangle:
    def draw(self):
        print("Drawing Rectangle")


class Car:
    def draw(self):
        print("Drawing Car")


def draw(shape):
    shape.draw()


# c = Circle()
# s = Square()
# r = Rectangle()
# car = Car()
#
# draw(c)
# draw(s)
# draw(r)
# draw(car)

# Q10.Design a polymorphic system for payment handling(UPI, Card, Cash) — all have a pay() method. Now implement a version that checks types
# explicitly using isinstance() before calling pay(). Compare both designs and explain why one breaks the spirit of polymorphism

class UPI:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Card:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")


class Cash:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")


def process_payment(method, amount):

    if isinstance(method, UPI):
        method.pay(amount)

    elif isinstance(method, Card):
        method.pay(amount)

    elif isinstance(method, Cash):
        method.pay(amount)

    else:
        print("Invalid Payment Method")


# process_payment(UPI(), 1000)
# process_payment(Card(), 2000)
# process_payment(Cash(), 500)

# Method Overriding Build a payment system with a base class Payment(amount) and three subclasses:
# CreditCard, UPI, and NetBanking. Each overrides a method process() with its own logic.
# Write a function checkout(payment) that calls process() on any payment object and demonstrate polymorphism.
class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        print(f"Processing payment of ₹{self.amount}")


class CreditCard(Payment):
    def process(self):
        print(f"Paid ₹{self.amount} using Credit Card")


class UPI(Payment):
    def process(self):
        print(f"Paid ₹{self.amount} using UPI")


class NetBanking(Payment):
    def process(self):
        print(f"Paid ₹{self.amount} using Net Banking")


def checkout(payment):
    payment.process()


# Driver Code
# checkout(CreditCard(500))
# checkout(UPI(500))
# checkout(NetBanking(500))

# Duck Typing Create three completely unrelated classes: PDFReport, ExcelSheet, and EmailMessage.
# Each has a method send(). Write a function dispatch(item) that calls send() using duck typing.
# Prove that no inheritance is needed.
class PDFReport:
    def send(self):
        print("Sending PDF Report")


class ExcelSheet:
    def send(self):
        print("Sending Excel Sheet")


class EmailMessage:
    def send(self):
        print("Sending Email Message")


def dispatch(item):
    item.send()


# Driver Code
# dispatch(PDFReport())
# dispatch(ExcelSheet())
# dispatch(EmailMessage())

#Write a function total_area(shapes) that takes a list of any shape objects and returns their combined area.
# Use duck typing — any object with an area() method should work. Test with Circle, Rectangle, Triangle, and a custom class Hexagon.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Hexagon:
    def __init__(self, side):
        self.side = side

    def area(self):
        return (3 * 1.732 / 2) * self.side * self.side


def total_area(shapes):
    total = 0
    for i in shapes:
        total += i.area()
    return total


# Driver Code
# shapes = [
#     Circle(5),
#     Rectangle(4, 6),
#     Triangle(10, 8),
#     Hexagon(3)
# ]
#
# print("Total Area =", total_area(shapes))

