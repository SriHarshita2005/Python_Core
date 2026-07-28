#Create a base class Animal with a method sound(). Create a derived class Dog that overrides the sound() method.
# Demonstrate method overriding.

class Animal:
    def sound(self):
        print("Animal making sounds")
class Dog(Animal):
    def sound(self):
        print("Bow Bow")
# d=Dog()
# d.sound()

# Create class A with method show(). Create class B(A) that overrides show() and also calls the parent method using super().
class A:
    def show(self):
        print("A class")
class B(A):
    def show(self):
        print("B class")
        super().show()
# b=B()
# b.show()

# Create multi-level inheritance with classes A → B → C, each having a method display() printing the class name.
# Create object of C and call display(), showing method resolution.

class A:
    def display(self):
        print("A class")
class B(A):
    def display(self):
        print("B class")
class C(B):
    def display(self):
        print("C class")
# c=C()
# c.display()
# print(C.mro())

#Implement hierarchical inheritance using a base class Vehicle and two child classes Car and Bike, each defining a method wheels().

class Vehicle:
    def wheels(self):
        print("Vehicle has wheels")
class Car(Vehicle):
    def wheels(self):
        print("car has 4 wheels")
class Bike(Vehicle):
    def wheels(self):
        print("bike has 2 wheels")
# c=Car()
# c.wheels()
# b=Bike()
# b.wheels()

#• Create class Employee with an instance method salary(). Create class Manager(Employee) that overrides salary() and adds an incentive. Demonstrate both outputs.

class Employee:
    def salary(self):
        print("Employee salary is 50000")
class Manager(Employee):
    def salary(self):
        print("employee salary is 50000 and incentives is 10000")
# e=Employee()
# e.salary()
# m=Manager()
# m.salary()

#Create class University with a class variable and a class method. Inherit it into class College and access the parent’s class variable from the child class.

class University:
    name='JNTU'
    @classmethod
    def show_university(cls):
        print("university:",cls.name)
class College(University):
    pass
# c=College()
# c.show_university()
# print(c.name)

#Create class MathOps with a static method add(a, b). Create class AdvancedOps(MathOps) and use the static method without overriding it.
class MathOps:
    @staticmethod
    def add(a,b):
        return a+b
class AdvancesOps(MathOps):
    pass
# print(AdvancesOps.add(10,20))
# m=AdvancesOps()
# print(m.add(20,30))

#Create two classes Father and Mother, both defining a method skills(). Create class Child(Father, Mother) and check which skills() runs using MRO.
class Father:
    def skills(self):
        print("Father's skills")
class Mother:
    def skills(self):
        print("Mother's skills")
class Child(Father,Mother):
    pass
# c=Child()
# c.skills()
# print(Child.mro())

#Create an abstract class Shape with an abstract method area(). Create class Rectangle(Shape) that implements the area() method.

from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self,l,b):
        return l*b
# r=Rectangle()
# print(r.area(10,5))

# Create class Person with a constructor __init__(name). Create class Student(Person) with constructor __init__(name, roll). Use super() to call the parent constructor.
class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):

    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)

# s = Student("Harshita", 101)
#
# s.display()


#Multi-level Inheritance Create a class Vehicle with attributes make, model, and year, and a method info().
# Create a child class Car(Vehicle) that adds a doors attribute and overrides info() to include doors.
# Create ElectricCar(Car) that adds battery_range and calls super().info() to extend the output. Demonstrate all three levels.
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"


class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def info(self):
        return f"{super().info()}, Doors: {self.doors}"


class ElectricCar(Car):
    def __init__(self, make, model, year, doors, battery_range):
        super().__init__(make, model, year, doors)
        self.battery_range = battery_range

    def info(self):
        return f"{super().info()}, Battery Range: {self.battery_range} km"


# Driver Code

# v = Vehicle("Toyota", "Corolla", 2020)
# print(v.info())
#
# c = Car("Honda", "City", 2022, 4)
# print(c.info())
#
# e = ElectricCar("Tesla", "Model 3", 2024, 4, 500)
# print(e.info())

# Build a multiple inheritance scenario: class Printable with a method print_info(), class Saveable with save().
# Create class Document(Printable, Saveable) that uses both. Print the MRO and explain the resolution order
class Printable:
    def print_info(self):
        print("Printing document information")


class Saveable:
    def save(self):
        print("Document saved")


class Document(Printable, Saveable):
    pass


# Driver Code
# doc = Document()
#
# doc.print_info()
# doc.save()
#
# # MRO
# print(Document.mro())

# Diamond Problem + MRO Create the classic diamond problem: A → B, A → C, D(B,C).
# Give all four classes a method hello() that returns their name. Show which hello() gets called on D().
# Then remove hello() from B and show how the MRO changes the result.
class A:
    def hello(self):
        return "A"


class B(A):
    def hello(self):
        return "B"


class C(A):
    def hello(self):
        return "C"


class D(B, C):
    pass


# d = D()
#
# print(d.hello())
# print(D.mro())

# super() Chaining Write a class hierarchy School → Department → Course. Use super() in every __init__ to chain initialisation correctly.
# Each class adds one attribute. Prove that Manager(super()) in one class correctly delegates through the full chain.
class School:
    def __init__(self, school_name):
        print("School __init__ called")
        self.school_name = school_name


class Department(School):
    def __init__(self, school_name, dept_name):
        print("Department __init__ called")
        super().__init__(school_name)
        self.dept_name = dept_name


class Course(Department):
    def __init__(self, school_name, dept_name, course_name):
        print("Course __init__ called")
        super().__init__(school_name, dept_name)
        self.course_name = course_name

    def display(self):
        print(f"School: {self.school_name}")
        print(f"Department: {self.dept_name}")
        print(f"Course: {self.course_name}")


# Driver Code
# c = Course("Vignan University", "CSE", "Python")
#
# c.display()

