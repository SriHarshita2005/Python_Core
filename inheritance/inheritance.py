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
