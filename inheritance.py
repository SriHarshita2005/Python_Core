class A:
    x=10
    def m1(self):
        print("A class")
class B(A):
    y=20
    def m1(self):
        print("B")
        super().m1()
# obj1=B()
# obj1.m1()


class A:
    @classmethod
    def m1(cls):
        print("A class")
class B(A):
    @classmethod
    def m2(cls):
        super().m1()
        print("B class")
class C(B):
    @classmethod
    def m1(cls):
        print("Class C")
        super(B,cls).m1()
c=C()
c.m1()


#  Create a base class Animal with a method sound(). Create a derived class Dog that overrides the sound() method.
# Demonstrate method overriding.

class Animal:
    def sound(self):
        print("Animals make sounds")
class Dog(Animal):
    def sound(self):
        print("Dogs bark")
        super().sound()
# a=Animal()
# a.sound()
# d=Dog()
# d.sound()


#• Create class A with method show(). Create class B(A) that overrides show() and also calls the parent method using super().
class A:
    def show(self):
        print("A class")
class B(A):
    def show(self):
        print("Class B")
        super().show()
# a=A()
# a.show()
# b=B()
# b.show()


# Create multi-level inheritance with classes A → B → C, each having a method display() printing the class name.
# Create object of C and call display(), showing method resolution.

class A:
    def display(self):
        print("Class A")
class B:
    def display(self):
        print("Class B")
class C:
    def display(self):
        print("Class C")
# c=C()
# c.display()


 #Implement hierarchical inheritance using a base class Vehicle and two child classes Car and Bike, each defining a method wheels().

class Vehicle:
     def show(self):
         print("This is vehicle")
class Car(Vehicle):
    def display(self):
        print("Car has 4 wheels")
class Bike(Vehicle):
    def display(self):
        print("Bike has 2 wheels")
# c=Car()
# c.display()
# c.show()
# b=Bike()
# b.display()
# b.show()


#Create class Employee with an instance method salary(). Create class Manager(Employee) that overrides salary() and adds an incentive.
#Demonstrate both outputs.

class Employee:
    def salary(self):
        salary=30000
        print(f"employee salary:{salary}")
class Manager(Employee):
    def salary(self):
        incentives=10000
        salary=30000
        total_salary=incentives+salary
        print(f"Total salary:{total_salary}")
# e=Employee()
# e.salary()
# m=Manager()
# m.salary()


#Create class University with a class variable and a class method. Inherit it into class College and access the parent’s class
# variable from the child class.

# class University:
#     university="JNTU"
#     def display(self):
#         print("University is JNTU")
# class College(University):

