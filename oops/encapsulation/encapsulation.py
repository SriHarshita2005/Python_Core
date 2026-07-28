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


# a = Attendance()
#
# a.mark_present("Harshita")
#
# print(a.view_attendance())

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


# s = Student(80)
#
# print(s.marks)
#
# s.marks = 95
# print(s.marks)
#
# s.marks = 150

#Design a BankAccount class with a private __balance. Create @property balance as a getter. Create a @balance.setter that raises ValueError if the value is negative. Add methods deposit(amount) and withdraw(amount) that update balance through the setter. Test all edge cases.
class BankAccount:
    def __init__(self,bal):
        self.__bal = bal
    @property
    def get_bal(self):
        return self.__bal
    @get_bal.setter
    def get_bal(self,nb):
        if nb <0 :
            raise ValueError("Balance is negative")
        self.__bal = nb
        return self.__bal
    def deposit(self,amount):
        if amount > 0:
            self.__bal += amount
            return self.__bal
        else:
            print("Amount cannot be negative")
    def withdraw(self,amount):
        if amount < self.__bal:
            self.__bal -= amount
            return self.__bal
        else:
            print("Balance becomes negative")
# b=BankAccount(100)
# print(b.get_bal)
# b.deposit(200)
# print(b.get_bal)
# b.withdraw(200)
# print(b.get_bal)

# Create a class Circle with a private __radius. Add @property radius (getter) and @radius.setter that validates the radius is positive. Add a computed @property area and @property circumference. Show that changing radius automatically updates both computed properties.
class Circle:
    def __init__(self,radius):
        self.__radius = radius
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self,nr):
        if nr>0:
            self.__radius=nr
            return self.__radius
    @property
    def get_area(self):
        return 3.14*self.__radius*self.__radius
    @property
    def circumfrence(self):
        return 2*3.14*self.__radius
# c=Circle(10)
# print(c.get_area)
# print(c.circumfrence)
# c.radius = 20
# print(c.get_area)
# print(c.circumfrence)

# Write a class Config with protected _settings dict and private __secret_key. Demonstrate: (a) public attribute access, (b) protected access with a warning comment, (c) private access via name mangling (and explain why you should NOT do this in real code), (d) a safe public method get_setting(key) as the correct approach.
class Config:
    def __init__(self):
        # Public attribute
        self.version = "1.0"

        # Protected attribute
        self._settings = {
            "theme": "dark",
            "language": "English"
        }

        # Private attribute
        self.__secret_key = "ABC123XYZ"

    # Safe public method
    def get_setting(self, key):
        return self._settings.get(key, "Setting not found")


# Driver Code
config = Config()

# (a) Public attribute access
print("Version:", config.version)

# (b) Protected attribute access
# Warning: Possible, but should be treated as internal use only.
print("Settings:", config._settings)

# (c) Private attribute access via name mangling
# Warning: This bypasses encapsulation and should NOT be done in real code.
print("Secret Key:", config._Config__secret_key)

# (d) Correct approach: use a public method
print("Theme:", config.get_setting("theme"))
print("Language:", config.get_setting("language"))

# Build a Person class using @property for first_name, last_name, and full_name. full_name should be a computed read-only property. Add a @full_name.setter that splits the input string on a space and updates first and last names separately.
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, value):
        first, last = value.split(" ")
        self.first_name = first
        self.last_name = last


# Driver Code
p = Person("Harshita", "Ganapathiraju")

print(p.first_name)
print(p.last_name)
print(p.full_name)

p.full_name = "Sai Kumar"

print("\nAfter updating full_name:")
print(p.first_name)
print(p.last_name)
print(p.full_name)














