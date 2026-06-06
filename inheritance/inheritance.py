#Create a base class Animal with a method sound(). Create a derived class Dog that overrides the sound() method.
# Demonstrate method overriding.

class Animal:
    def sound(self):
        print("Animals make sounds")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
# d=Dog()
# d.sound()
# a=Animal()
# a.sound()

# Create class A with method show(). Create class B(A) that overrides show() and also calls the parent method using super().
class A:
    def show(self):
        print("This is A class")
class B(A):
    def show(self):
        print("This is B class")
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
        print("Car has 4 wheels")
class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels")
# c=Car()
# c.wheels()
# b=Bike()
# b.wheels()

#• Create class Employee with an instance method salary(). Create class Manager(Employee) that overrides salary() and adds an incentive. Demonstrate both outputs.
class Employee:
    def salary(self):
        print("Salary = 50000")
class Manager(Employee):
    def salary(self):
        print("Salary = 50000 + Incentives = 10000")
# e=Employee()
# e.salary()
# m=Manager()
# m.salary()

#Create class University with a class variable and a class method. Inherit it into class College and access the parent’s class variable from the child class.
class University:
    university_name="JNTU"
    @classmethod
    def show_university(cls):
        print("University: ",cls.university_name)
class College(University):
    pass
# print(College.university_name)
# College.show_university()

#Create class MathOps with a static method add(a, b). Create class AdvancedOps(MathOps) and use the static method without overriding it.
class MathOps:
    @staticmethod
    def add(a,b):
        return a+b
class AdvancesOps(MathOps):
    @staticmethod
    def add(a,b):
        return a+b
# print(AdvancesOps.add(10,20))
# obj=AdvancesOps()
# print(obj.add(30,20))

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

s = Student("Harshita", 101)

s.display()