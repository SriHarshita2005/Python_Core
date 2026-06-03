
# class A:
#     def __init__(self,x):
#         self.x=x
#     def __add__(self, o2):
#         return self.x+o2
# a1=A(10)
# print(a1+20)


# class B:
#     def __init__(self,x):
#         self.x=x
#     def __add__(self, other):
#         return self.x+other.x
# b1=B(30)
# b2=B(35)
# print(b1+b2)

#using is_instance method for checking whether it is in same class or not
# class B:
#     def __init__(self,x):
#         self.x=x
#     def __add__(self, other):
#         if isinstance(other,int):
#             return self.x+other
#         elif isinstance(other,B):
#             return self.x+other.x
#         else:
#             print("Wrong class")
#             return 0
# b1=B(50)
# b2=B(25)
# print(b1+b2)
# print(b1+50)
# print(b1+1.34)

# class C:
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
#     def __add__(self, other):
#         if isinstance(other,str):
#             return self.x+other
#         if isinstance(other,int):
#             return self.y+other
#         if isinstance(other,C):
#             return self.z+other.z
#         else:
#             print("Wrong number")
#             return 0
# c1=C("Hello",10,20)
# c2=C("H1",60,40)
# print(c1+c2)
# print(c1+75)
# print(c1+"Hello")


# class C:
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
#     def __sub__(self, other):
#         if isinstance(other,str):
#             return self.x-other
#         if isinstance(other,int):
#             return self.y-other
#         if isinstance(other,C):
#             return self.z-other.z
#         else:
#             print("Wrong number")
#             return 0
# c1=C("Hello",10,20)
# c2=C("H1",60,40)
# print(c1-c2)
# print(c1-75)
# print(c1-"Hello")


# class D:
#     def __str__(self):
#         return "THIS IS D CLASS"
#
#     def __repr__(self):
#         return "This is repr"
# d1=D()
# print(d1)
# print([d1])


# class C:
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
#     def __add__(self, other):
#         if isinstance(other,str):
#             return self.x+other
#         if isinstance(other,int):
#             return self.y+other
#         if isinstance(other,C):
#             return self.z+other.z
#         else:
#             print("Wrong number")
#             return 0
#     def __str__(self):
#         return f"x:{self.x}\ny:{self.y}\nz:{self.z}"
#     def __repr__(self):
#         return f"x:{self.x}\ny:{self.y}\nz:{self.z}"
#
# c1=C("Hello",10,20)
# c2=C("H1",60,40)
# print(c1+c2)
# print(c1+75)
# print(c1+"Hello")
# c3=C("Hello",10,20)
# print(c3)

class E:
    def __init__(self,a):
        self.a=a
    def __gt__(self, other):
        return self.a>other.a
    def __lt__(self, other):
        return self.a<other.a
    def __ge__(self, other):
        return self.a>=other.a
    def __le__(self, other):
        return self.a<=other.a
    def __eq__(self, other):
        return self.a==other.a
    def __ne__(self, other):
        return self.a!=other.a
# e1=E(25)
# e2=E(35)
# print(e1>e2)
# print(e1<e2)
# print(e1>=e2)
# print(e1<=e2)
# print(e1==e2)
# print(e1!=e2)


# create a class vector with x,y,coordinates : compare their distances from (0,0) and perform all operations
import math
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def check(self):
        return math.sqrt((self.x**2+self.y**2))
    def __str__(self):
        return f"X COORDINATES:{self.x} , Y coordinates:{self.y}"
    def __add__(self, other):
        return Vector(self.x+other.x,self.y+other.y)
    def __sub__(self, other):
        return Vector(self.x-other.x,self.y-other.y)
    def __gt__(self, other):
        return self.check()>other.check()
    def __lt__(self, other):
        return self.check()<other.check()
    def __ge__(self, other):
        return self.check()>=other.check()
    def __le__(self, other):
        return self.check()<=other.check()
    def __eq__(self, other):
        return self.check()==other.check()
# v1=Vector(10,20)
# v2=Vector(20,30)
# v3=Vector(10,20)
# print(v1)
# print(v2)
# print(v1+v2)
# print(v1+v2+v3)
# print(v1-v2)
# print(v1>v2)
# print(v1<v2)
# print(v1>=v2)
# print(v1<=v2)
# print(v1==v2)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


# class Cart:
#     def __init__(self):
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#
#     def display(self):
#         for p in self.products:
#             print("Name:", p.name)
#             print("Price:", p.price)
#             print("Quantity:", p.quantity)
#             print()
#
#
# # Product object
# p1 = Product("Laptop", 50000, 2)
#
# # Cart object
# c1 = Cart()
#
# # Add product to cart
# c1.add_product(p1)
#
# # Display cart products
# c1.display()

#create a class product with name , price, quantity. Create a class cart that stores the products
#c1 as cart class obj and p1 as product class obj
# c1+p1 ---> adds products into cart
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def __str__(self):
        return f"Name:{self.name}\nPrice:{self.price}\nQuantity:{self.quantity}"

class Cart:
    def __init__(self):
        self.l=[]
    def __add__(self, other):
        self.l.append(other)
        return self
    def __sub__(self, other):
        if other in self.l:
            self.l.remove(other)
        return self
    def total_price(self):
        s=0
        for i in self.l:
            s+=(i.price*i.quantity)
        return s
    def __str__(self):
        for i in self.l:
            print(i)
        print(f"Total Products:{len(self.l)}")
        print(f"Total_price:{self.total_price()}")
        return "Thanks for products"
# p1=Product("BOOK", 100,10)
# c1=Cart("Book",100,3)
#
# print(p1)



# Question 1: Bank Account Operations
# Create a class BankAccount with:
# attributes: account_holder, balance
# instance method: deposit(amount)
# instance method: withdraw(amount)
# Implement these magic methods:
# __str__() → display account details
# __add__() → add balances of two accounts
# __sub__() → subtract balances
# __eq__() → compare if two accounts have same balance
# __lt__() → check which account has lower balance
# __getattribute__() → print a message whenever an attribute is accessed
# __setattr__() → prevent setting negative balance
# Demonstrate creating two accounts and using all operations.

class BankAccount:
    def __init__( self , account_holder , balance ):
        self.account_holder = account_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposited:", amount)
    def withdraw(self,amount):
        if(self.balance>=amount):
            self.balance-=amount
            print("Withdrawn amount:",amount)
        else:
            print("Insufficient balance")
    def __str__(self):
        return f"Name:{self.account_holder} , Balance:{self.balance}"
    def __add__(self, other):
        return self.balance + other.balance
    def __sub__(self, other):
        return self.balance-other.balance
    def __eq__(self, other):
        return self.balance == other.balance
    def __lt__(self, other):
        return self.balance < other.balance
    def __getattribute__(self, name):
        print(f"Accessing attribute{name}")
        return object.__getattribute__(self,name)
    def __setattr__(self, name, value):
        if name=="balance" and value<0:
            print("Negative balance is not allowed")
        else:
            return object.__setattr__(self,name,value)
# acc1=BankAccount("Harshita",5000)
# acc2=BankAccount("Ravi",3000)
# print(acc1)
# print(acc2)
# acc1.deposit(2000)
# acc2.withdraw(1000)
# print("Total Balance:",acc1+acc2)
# print("Balance Difference:", acc1 - acc2)
# print("Same Balance:",acc1==acc2)
# print("Acc1 has lower balance:",acc1<acc2)
# print(acc1.balance)
# acc1.balance=-500

# Question 2: Product Price Comparison
# Create a class Product with:
# attributes: name, price, quantity
# method: total_price()
# Implement:
# __str__()
# __add__() → add total prices of two products
# __mul__() → multiply product price by a number
# __gt__() → compare which product has greater total value
# __eq__() → compare prices
# __getattr__() → return "Attribute not found" for missing attributes
# __setattr__() → do not allow price less than 0

class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def total_price(self):
        return self.price*self.quantity
    def __str__(self):
        return f"Product:{self.name} , Price:{self.price} , Quantity:{self.quantity} , Total Price:{self.total_price()}"
    def __add__(self, other):
        return self.total_price()+other.total_price()
    def __mul__(self, other):
        return self.price*other
    def __gt__(self, other):
        return self.total_price()>other.total_price()
    def __eq__(self, other):
        return self.price==other.price
    def __getattr__(self, name):
        return "Attribute not found"
    def __setattr__(self, name, value):
        if name=="price" and value<0:
            print("Negative prices not allowed")
        else:
            return object.__setattr__(self,name,value)
# p1=Product("Laptop",50000,2)
# p2=Product("Phone",30000,3)
# print(p1)
# print(p2)
# print("Total price of p1:", p1.total_price())
# print("Total price of p2:", p2.total_price())
# print("Added total price is:",p1+p2)
# print("Price multiplied:",p1*2)
# print("P1 greater than p2:",p1>p2)
# print("P1 is equal to p2:",p1==p2)
# print(p1.color)
# p1.price=-10000

# Question 3: Student Marks
# Create a class Student with:
# attributes: name, marks
# method: grade()
# Implement:
# __str__()
# __add__() → add marks of two students
# __truediv__() → divide marks by a number
# __ge__() → check if one student scored greater than or equal to another
# __lt__() → check if one student scored less
# __getattribute__() → track attribute access
# __setattr__() → marks must be between 0 and 100

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def grade(self):
        if self.marks>=90:
            return "A"
        elif self.marks>=70:
            return "B"
        elif self.marks>=50:
            return "C"
        else:
            return "D"
    def __str__(self):
        return f"Name:{self.name} , Marks:{self.marks} , Grade:{self.grade()}"
    def __add__(self, other):
        return self.marks+other.marks
    def __truediv__(self, other):
        return self.marks/other
    def __ge__(self, other):
        return self.marks>=other.marks
    def __lt__(self, other):
        return self.marks<other.marks
    def __getattribute__(self, name):
        print(f"Accessing attributes:{name}")
        return object.__getattribute__(self,name)
    def __setattr__(self, name, value):
        if name=="marks" and (value<0 or value>100):
            print("Marks should be in the range 0 to 100")
        else:
            return object.__setattr__(self,name,value)
# s1 = Student("Harshita", 92)
# s2 = Student("Ravi", 78)
# print(s1)
# print(s2)
# print("Total Marks:", s1 + s2)
# print("Divided Marks:", s1 / 2)
# print("s1 >= s2:", s1 >= s2)
# print("s1 < s2:", s1 < s2)
# print(s1.marks)
# s1.marks = 150


# Question 4: Rectangle Area Comparison
# Create a class Rectangle with:
# attributes: length, breadth
# method: area()
# Implement:
# __str__()
# __add__() → add areas of two rectangles
# __sub__() → subtract areas
# __eq__() → compare areas
# __gt__() → check which rectangle has larger area
# __getattr__() → handle missing attributes
# __setattr__() → length and breadth must be positive
#
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def __str__(self):
        return f"Length:{self.length} , Breadth:{self.breadth} , Area:{self.area()}"
    def __add__(self, other):
        return self.area()+other.area()
    def __sub__(self, other):
        return self.area() - other.area()
    def __eq__(self, other):
        return self.area() == other.area()
    def __gt__(self, other):
        return self.area() > other.area()
    def __getattr__(self, name):
        return "Attribute not found"
    def __setattr__(self, name, value):
        if (name=="length" and value<0) or (name=="breadth" and value<0):
            print("Length and Breadth must be positive")
        else:
            return object.__setattr__(self,name,value)
# r1=Rectangle(10,20)
# r2=Rectangle(20,40)
# print(r1)
# print(r2)
# print(r1+r2)
# print(r1-r2)
# print(r1==r2)
# print(r1>r2)
# print(r1.radius)
# r1.length=-30


# Question 5: Employee Salary System
# Create a class Employee with:
# attributes: name, salary
# method: annual_salary()
# Implement:
# __str__()
# __add__() → add salaries of two employees
# __mul__() → calculate salary after multiplying by months
# __ne__() → check if salaries are not equal
# __le__() → check if one salary is less than or equal to another
# __getattribute__() → log every attribute access
# __setattr__() → salary cannot be below 10000

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def annual_salary(self):
        return self.salary*12
    def __str__(self):
        return f"Name:{self.name} , Salary:{self.salary} , Annual Salary:{self.annual_salary()}"
    def __add__(self, other):
        return self.salary+other.salary
    def __mul__(self, other):
        return self.salary*other
    def __ne__(self, other):
        return self.salary!=other.salary
    def __le__(self, other):
        return self.salary<=other.salary
    def __getattribute__(self, name):
        print(f"Accessing attribute:{name}")
        return object.__getattribute__(self,name)
    def __setattr__(self, name, value):
        if name=="salary" and value<10000:
            print("Salary should be more than 10000")
        else:
            object.__setattr__(self,name,value)
# e1=Employee("Harshita",100000)
# e2=Employee("Ravi",50000)
# print(e1)
# print(e2)
# print(e1+e2)
# print(e1*2)
# print(e1!=e2)
# print(e1<=e2)
# e2.salary=5000


# Question 6: Book Object Comparison
# Create a class Book with:
# attributes: title, author, pages
# method: reading_time()
# Assume 1 page takes 2 minutes.
# Implement:
# __str__()
# __add__() → add pages of two books
# __floordiv__() → divide pages by number of days
# __gt__() → compare books based on pages
# __eq__() → compare books based on title
# __getattr__() → return custom message for missing attribute
# __setattr__() → title cannot be empty and pages must be positive

class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def reading_time(self):
        return self.pages*2
    def __str__(self):
        return f"Title:{self.title} , Author:{self.author} , Pages:{self.pages} , Reading Time:{self.reading_time()}"
    def __add__(self, other):
        return self.pages+other.pages
    def __floordiv__(self, other):
        return self.pages//other
    def __gt__(self, other):
        return self.pages>other.pages
    def __eq__(self, other):
        return self.title==other.title
    def __getattr__(self, name):
        return "Attribute is missing"
    def __setattr__(self, name, value):
        if name=="title" and value=="" or name=="pages" and value<0:
            print("Invalid")
        else:
            object.__setattr__(self,name,value)
# b1=Book("House Of Cards",'Sudha Murthy',300)
# b2=Book("Gently falls the bakula",'Sudha Murthy',300)
# print(b1)
# print(b2)
# print(b1+b2)
# print(b1//3)
# print(b1>b2)
# print(b1==b2)
# print(b1.name)
# b1.title=""



# Question 7: Shopping Cart
# Create a class CartItem with:
# attributes: item_name, price, quantity
# method: final_amount()
# Implement:
# __str__()
# __add__() → add final amounts of two cart items
# __mod__() → find remainder after applying a discount value
# __lt__() → compare item total amount
# __ge__() → compare quantity
# __getattribute__() → display which attribute is being accessed
# __setattr__() → quantity cannot be less than 1

class CartItem:
    def __init__(self,item_name,price,quantity):
        self.item_name=item_name
        self.price=price
        self.quantity=quantity
    def final_amount(self):
        return self.price*self.quantity
    def __str__(self):
        return f"Name:{self.item_name} , Price:{self.price} , Quantity:{self.quantity} , FinalAmount:{self.final_amount()}"
    def __add__(self, other):
        return self.final_amount()+other.final_amount()
    def __mod__(self, other):
        return self.final_amount()%other
    def __lt__(self, other):
        return self.final_amount()<other.final_amount()
    def __ge__(self, other):
        return self.final_amount()>=other.final_amount()
    def __getattribute__(self, item):
        print(f"Accessing attribute:{item}")
        return object.__getattribute__(self,item)
    def __setattr__(self, name, value):
        if name=="quantity" and value<1:
            print("Give quantity more than 1")
        else:
            return object.__setattr__(self,name,value)
# c1=CartItem("Milk",40,5)
# c2=CartItem("Tea",5,10)
# print(c1)
# print(c2)
# print(c1+c2)
# print(c1%10)
# print(c1<c2)
# print(c1>=c2)
# c1.quantity=0


# Question 8: Time Duration
# Create a class TimeDuration with:
# attributes: hours, minutes
# method: total_minutes()
# Implement:
# __str__()
# __add__() → add two time durations
# __sub__() → subtract two time durations
# __eq__() → compare total minutes
# __gt__() → check longer duration
# __getattr__() → handle invalid attribute access
# __setattr__() → minutes must be between 0 and 59


class TimeDuration:
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
    def total_minutes(self):
        return self.hours*self.minutes
    def __str__(self):
        return f"Hours:{self.hours} , Minutes:{self.minutes} , Total Minutes:{self.total_minutes()}"
    def __add__(self, other):
        return self.hours+other.minutes
    def __sub__(self, other):
        return self.hours-other.minutes
    def __eq__(self, other):
        return self.minutes==other.minuts
    def __gt__(self, other):
        return self.total_minutes()>other.total_minutes()
    def __getattr__(self, item):
        return "Invalid attribute access"
    def __setattr__(self, key, value):
        if key=="minutes" and (value<0 or value>59):
            print("Minutes must be 0 to 59")
        else:
            return object.__setattr__(self,key,value)
# t1=TimeDuration(2,30)
# t2=TimeDuration(3,45)
# print(t1)
# print(t2)
# print(t1+t2)
# print(t2-t1)
# print(t1==t2)
# print(t1>t2)
# print(t1.sec)
# t1.minutes=60


# Question 9: Laptop Specification
# Create a class Laptop with:
# attributes: brand, ram, price
# method: upgrade_ram(extra_ram)
# Implement:
# __str__()
# __add__() → add prices of two laptops
# __mul__() → multiply price for bulk purchase
# __lt__() → compare price
# __eq__() → compare RAM
# __getattribute__() → print access message
# __setattr__() → RAM and price must be positive

class Laptop:
    def __init__(self,brand,ram,price):
        self.brand=brand
        self.ram=ram
        self.price=price
    def update_ram(self,extra_ram):
        self.ram = self.ram + extra_ram
        print("Ram Updated")
        return self.ram
    def __str__(self):
        return f"Brand:{self.brand} , Ram:{self.ram} , Price:{self.price}"
    def __add__(self, other):
        return self.price+other.price
    def __mul__(self, other):
        return self.price*other
    def __lt__(self, other):
        return self.price<other.price
    def __eq__(self, other):
        return self.ram==other.ram
    def __getattribute__(self, item):
        print(f"Accessing variable:{item}")
        return object.__getattribute__(self,item)
    def __setattr__(self, key, value):
        if key=="ram" and value<0:
            print("Ram must be positive")
        else:
            return object.__setattr__(self,key,value)
# l1=Laptop("HP",128,50000)
# l2=Laptop("Dell",130,60000)
# print(l1)
# print(l2)
# print(l1+l2)
# print(l1*5)
# print(l1<l2)
# print(l1==l2)
# l1.ram=-20

# Question 10: Game Player
# Create a class Player with:
# attributes: name, health, attack_power
# method: attack(enemy)
# Implement:
# __str__()
# __add__() → combine attack powers
# __sub__() → reduce health after attack
# __gt__() → compare health
# __eq__() → compare attack power
# __getattr__() → return custom message for unavailable player stat
# __setattr__() → health cannot go below 0

class Player:

    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, enemy):
        enemy.health = enemy.health - self.attack_power
        print(f"{self.name} attacked {enemy.name}")

    def __str__(self):
        return f"Name:{self.name}, Health:{self.health}, Attack Power:{self.attack_power}"

    def __add__(self, other):
        return self.attack_power + other.attack_power

    def __sub__(self, damage):
        self.health = self.health - damage
        return self.health

    def __gt__(self, other):
        return self.health > other.health

    def __eq__(self, other):
        return self.attack_power == other.attack_power

    def __getattr__(self, name):
        return f"{name} stat is not available"

    def __setattr__(self, name, value):

        if name == "health" and value < 0:
            object.__setattr__(self, name, 0)

        else:
            object.__setattr__(self, name, value)

#
# p1 = Player("Ravi", 100, 30)
# p2 = Player("Arjun", 80, 25)
#
# print(p1)
#
# p1.attack(p2)
#
# print(p2)
#
# print("Combined Attack Power:", p1 + p2)
#
# p1 - 40
#
# print("After Damage:", p1)
#
# print(p1 > p2)
#
# print(p1 == p2)
#
# print(p1.speed)
#
# p1.health = -50
#
# print(p1.health)




