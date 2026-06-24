#create a bank account with accno,balance:private,pin:private,name:protected and implement withdraw,
# deposit and display methods

class Bank:
    def __init__(self,a,b,p,name):
        self.a=a
        self.__b=b
        self.__p=p
        self._name=name
    def withdraw(self,amount):
        if self.__b<amount:
            print("Insufficient Balance")
        else:
            self.__b=self.__b-amount
            return self.__b
    def deposit(self,amount):
        self.__b=self.__b+amount
        return self.__b
        print("Amount deposited successfully")
    def display(self):
        p=int(input("Enter pin:"))
        if p==self.__p:
            print(f"Account number={self.a}, Balance:{self.__b}, ")
        else:
            print("Enter correct pin")
# b1=Bank(1233000,1234,1234,"Harshitha")
# b1.withdraw(500)
# b1.deposit(100000)
# b1.display()

# 1. Create a BankAccount class that stores:
# • account number
# • balance (should not be directly modifiable)
# You must:
# 1. Make the balance attribute inaccessible from outside.
# 2. Provide functions to deposit/withdraw that validate the amount.
# 3. Prevent withdrawal if balance becomes negative.
# 4. Show what happens if someone tries to modify balance directly and why
# encapsulation prevents it.

class BankAccount:
    def __init__(self,accno,bal):
        self.accno=accno
        self.__bal=bal
    def deposit(self,amount):
        if amount>0:
            self.__bal+=amount
            return self.__bal
    def withdraw(self,amount):
        if amount<=self.__bal:
            self.__bal-=amount
            return self.__bal
        else:
            print("Balance becomes negative")
    def show_bal(self,):
        return self.__bal
# b=BankAccount(100,1000)
# print(b.deposit(1000))
# print(b.withdraw(1500))
# print(b.show_bal())

# 2. Design a Student class where marks:
# • should always be between 0 and 100
# • should never be set directly
# Enable updating marks only through a controlled method that performs range
# checks.
# Demonstrate:
# • trying to assign marks manually
# • why encapsulation protects invalid states

class Student:
    def __init__(self,marks):
        if 0<= marks <=100:
            self.__marks=marks
        else:
            print("Invalid Marks")
            self.__marks=0
    def update(self,new_marks):
        if 0< new_marks<100:
            self.__marks = new_marks
            print("Marks updated")
        else:
            print("Invalid marks")
    def get_marks(self):
        return self.__marks

# s = Student(90)
# print(s.get_marks())
# s.__marks= 40
# print(s.get_marks())
# s.update(120)
# print(s.get_marks())

# 3. Create a SecureFile class that:
# • stores content privately
# • provides a method read(password)
# • refuses access if the password is incorrect
# • logs an "Unauthorized attempt" internally (cannot be accessed from outside)

class SecureFile:
    def __init__(self,content,password):
        self.__content=content
        self.__password = password
        self.__log=[]
    def read(self,password):
        if password == self.__password:
            return self.__content
        else:
            self.__log.append("Unauthorised attempt")
            return "Access denied"
# s1=SecureFile("Python","1234")
# print(s1.read("1234"))
# print(s1.read(1111))

# 4.Design an Employee class where:
# • salary is hidden
# • outsiders cannot read salary directly
# • use getter method that logs each access attempt
# • provide a method to update salary but only if the new salary is higher (prevent
# accidental downgrade)

class Employee:
    def __init__(self,salary):
        self.__salary=salary
        self.__log=[]
    def get_salary(self):
        self.__log.append("Salary appended")
        return self.__salary
    def update_salary(self,new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
            print("Salary updated")
        else:
            print("New salary must be higher than current salary")
# e1 = Employee(50000)
# print("Salary:", e1.get_salary())
# e1.update_salary(60000)
# print("Updated Salary:", e1.get_salary())
# e1.update_salary(45000)

# 5. Create a Product class where:
# • price cannot be negative
# • discount cannot exceed 70%
# • internal final price calculation should not be directly exposed
# Provide only one public method get_final_price().

class Product:
    def __init__(self,price,discount):
        if price<0:
            print("Price cannot be negative")
            self.__price=0
        else:
            self.__price=price
        if  0 < discount < 70:
            self.__discount=discount
        else:
            print("Discount must be between 0 and 70")
            self.__discount=0
    def __calculate_final_price(self):
        return self.__price - (self.__price * self.__discount / 100)
    def get_price(self):
        return self.__calculate_final_price()
# p1=Product(1000,20)
# p1.get_price()
# p2=Product(-500,80)
# p2.get_price()

# 6. Create a Character class with:
# • private _health
# • methods to damage(points) and heal(points)
# • health cannot drop below 0 or exceed max limit
# • expose only current health through a read-only getter

class Character:
    def __init__(self,health,max_health):
        self.__max_health=max_health
        if 0< health<max_health:
            self.__health=health
        else:
            self.__health=max_health
    def damage(self,points):
        self.__health -= points
        if self.__health < 0:
            self.__health = 0
    def heal(self,points):
        self.__health += points
        if self.__health > self.__max_health:
            self.__health = self.__max_health
    def get_health(self):
        return self.__health
# c1 = Character(80, 100)
# print("Current Health:", c1.get_health())
# c1.damage(30)
# print("After Damage:", c1.get_health())
# c1.damage(100)
# print("After Heavy Damage:", c1.get_health())
# c1.heal(50)
# print("After Heal:", c1.get_health())
# c1.heal(100)
# print("After Excess Heal:", c1.get_health())

# 7. Create:
# • An Engine class with private state like temperature
# • A Car class that uses an Engine but should:
# o Not allow users to manipulate engine temperature
# o Only expose methods like start_car() or cool_engine()
# Demonstrate why giving direct engine access is dangerous.

class Engine:
    def __init__(self):
        self.__temperature = 25

    def start(self):
        self.__temperature += 30
        print("Engine Started")

    def cool(self):
        self.__temperature -= 10
        if self.__temperature < 25:
            self.__temperature = 25
        print("Engine Cooled")

    def get_temperature(self):
        return self.__temperature


class Car:
    def __init__(self):
        self.__engine = Engine()

    def start_car(self):
        self.__engine.start()

    def cool_engine(self):
        self.__engine.cool()

    def engine_status(self):
        return self.__engine.get_temperature()


# c = Car()
#
# c.start_car()
# print("Temperature:", c.engine_status())
#
# c.cool_engine()
# print("Temperature:", c.engine_status())

# 8. Create a ShoppingCart class where:
# • items are stored privately
# • users cannot directly modify item list
# • only add/remove methods are allowed
# • provide a method to get a safe copy of the cart items (not direct reference to internal
# list)

class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)

    def get_items(self):
        return self.__items.copy()      # Safe copy


# cart = ShoppingCart()
#
# cart.add_item("Laptop")
# cart.add_item("Mouse")
#
# items = cart.get_items()
# items.append("Mobile")      # Changes only copied list
#
# print("Cart Items:", cart.get_items())

# 9. Implement a class incorrectly first:
# • Attendance stored in a list
# • Exposed directly so any outside code can modify it
# Then redesign properly:
# • Make attendance private
# • Provide controlled methods for marking attendance only
# Explain the difference.

class Attendance:
    def __init__(self):
        self.__attendance = []

    def mark_present(self, student):
        self.__attendance.append(student)

    def view_attendance(self):
        return self.__attendance.copy()


a = Attendance()

a.mark_present("Harshita")

print(a.view_attendance())

# 10. Create a class using @property and @setter for a private attribute.
# Then:
# 1. Show correct usage
# 2. Show how forgetting to use underscore prefix breaks encapsulation
# 3. Show what happens if you implement a setter without validation
# Focus: Python-specific encapsulation pitfalls, misuse of properties

class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Invalid Marks")


s = Student(80)

print(s.marks)

s.marks = 95
print(s.marks)

s.marks = 150












