# 1. Write a Python program that attempts to dynamically import a module at runtime. The program should only import the module if it actually exists; otherwise, it should print "Module does not exist".

# import importlib
from importlib.util import find_spec
x = input("Enter module name")
try:
    y = importlib.import_module(x)
except ModuleNotFoundError:
    print("Module not found")

# k =find_spec(x)
# print(k)

#2. Create a Python package that contains two or more modules. Each module should define classes with attributes and methods. Then create another module outside the package, import the package modules, and create a subclass that inherits from at least one of the classes. Finally, create objects of both parent and child classes.

from mypackage.student import Student
from mypackage.teacher import Teacher

class Monitor(Student):
    def __init__(self, name, rollno):
        super().__init__(name)
        self.rollno = rollno

    def details(self):
        print("Roll No:", self.rollno)

# Parent class object
# s = Student("Harshita")
# s.display()

# Another parent class object
# t = Teacher("Python")
# t.show()

# Child class object
# m = Monitor("Anjali", 101)
# m.display()
# m.details()

#Create two Python modules that import each other. Run the program to observe what happens with circular imports. Then think of different ways to prevent a circular-import crash.

in a.py
localised import
def fun():
    import B
    print("Inside module B")
fun()

in b.py
def fun():
    import A
    print("Inside module A")
fun()

#Create a package with a module containing an abstract base class (ABC). Another module in the same package should define concrete subclasses that implement all abstract methods. Write a driver program that imports these classes and demonstrates polymorphism.
from shapes.circle import Circle, Square

# c = Circle()
# s = Square()
#
# c.area()
# s.area()

#5. Create three modules: Module A: class Animal Module B: class Walkable Module C: class Dog that inherits from both Animal and Walkable Demonstrate method resolution order (MRO) by calling overridden methods and printing the MRO.

# animal.py
# class Animal:
#     def sound(self):
#         print("Animal makes sounds")

# walkable.py
# class Walkable:
#     def sound(self):
#         print("Walking")
#
# dog.py
# from animal import Animal
# from walkable import Walkable

# class Dog(Animal, Walkable):
#     pass
#
# main.py
# from dog import Dog
# d = Dog()
# d.sound()
# print(Dog.mro())

#6. Create a class in a module that uses private attributes and @property / @setter decorators. Import the class into another module and show how encapsulation protects the data while still allowing controlled access.

class Bank:
    def __init__(self,accno):
        self.__accno = accno
    @property
    def show(self):
        return self.__accno
    @


#7. Create a module containing two classes where one uses composition and another uses inheritance to reuse code from a base class. Import and demonstrate the difference between the two approaches.