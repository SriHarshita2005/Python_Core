# • Create a class Person whose constructor takes age as an argument. Raise a
# ValueError if the age is less than 0.

class Person:
    def __init__(self,age):
        if age < 0:
            raise ValueError
        self.age = age
Person(25)

# • Write a function named find_length(obj) that uses a loop to calculate the
# length of the given object without using the built-in len() function. The
# function should return the calculated length if the object is iterable. If a
# non-iterable object such as an integer is passed, the function should raise and
# handle a TypeError, and print an appropriate error message explaining what
# happens when an integer is sent as input.

def find_len(obj):
    try:
        count = 0
        for i in obj:
            count+=1
        return count
    except TypeError as e:
        print("Pass only iterable values")
# l = [1,2,3,4,5]
# print(find_len(l))
# a = 122
# (find_len(a))

# • Create a class Student with an attribute marks. Implement a method
# set_marks(marks) that raises a ValueError if marks are not in the range 0 to
# 100.

class Student:
    def __init__(self,marks):
        self.set_marks(marks)
    def set_marks(self,new):
        if new<0 or new>100:
            raise ValueError
        else:
            self.marks = new
            return self.marks
# s = Student(101)
# print(s.marks)


# • Create a custom exception named InvalidAgeError. Create a class Voter with a
# method check_eligibility(age) that raises this exception if age is less than 18.

class InvalidAgeError(Exception):
    pass
class Voter:
    def check_eligibility(self,age):
        if age < 18:
            raise InvalidAgeError("Age is not eligible to vote")
        else:
            print("Eligible to vote")
# v = Voter()
# try:
#     age = int(input("Enter age"))
#     v.check_eligibility(age)
# except InvalidAgeError as e:
#     print(e)

# • Create a class BankAccount with an attribute balance. Implement a method
# withdraw(amount) that raises an exception if the withdrawal amount is greater
# than the available balance.

class BankAccount:
    def __init__(self,bal):
        self.bal = bal
    def withdraw(self,amount):
        if amount > self.bal:
            raise Exception("Insufficient balance")
        else:
            self.bal -= amount
            return self.bal
# b = BankAccount(5000)
# try:
#     print(b.withdraw(2000))
#     print(b.withdraw(6000))
# except Exception as e:
#     print(e)

# • Create a class PasswordValidator with a method validate(password). Raise an
# exception if the password length is less than 8 characters.

class PasswordValidator:
    def validate_password(self,password):
        if len(password) < 8:
            raise Exception("Password must be 8 length")
        else:
            return password
# p = PasswordValidator()
# try:
#     print(p.validate_password("adggbhgfergr"))
#     print(p.validate_password("1234"))
# except Exception as e:
#     print(e)

# • Create a class UserInput with a method get_integer(value). Handle ValueError
# and TypeError using separate except blocks.

class UserInput:
    def get_integer(self,value):
        try:
            return int(value)
        except ValueError:
            print("Value Error")
        except TypeError:
            print("Type Error")
# obj=UserInput()
# # obj.get_integer("abd")
# obj.get_integer(None)      # TypeError


# • Create a base class Shape with a method area() that raises
# NotImplementedError. Create a child class Rectangle that overrides and
# implements the area method.

class Shape:
    def area(self):
        raise NotImplementedError("Not implemented")
class Rectangle(Shape):
    def area(self,l,b):
        return l*b
# obj = Rectangle()
# print(obj.area(2,3))

# • Create a class Service with a method that calls another method which raises an
# exception. Catch and handle the exception in the Service class.

class Service:
    def method1(self):
        raise Exception("Method calling")
    def method2(self):
        try:
            self.method1()
        except Exception as e:
            print(e)
# obj = Service()
# obj.method2()

# • Create a class Transaction with a method process() that uses try, except, and
# finally blocks to ensure a cleanup message is always printed.

class Transaction:
    def process(self,amount):
        try:
            if amount < 0:
                raise Exception("Amount should be positive")
            else:
                print("Successful")
        except Exception :
            print("Value error")
        finally:
            print("Code completed")
# obj = Transaction()
# obj.process(-100)
# obj.process(23)

# • Create a class LoginSystem with a method login(password) that raises an
# exception for an incorrect password and handles the exception outside the class.

class LoginSystem:
    def login(self,password):
        if password != "admin123":
            raise Exception("Incorrect Password")
        print("Login Successful")
        obj = LoginSystem()
        try:
            obj.login(input("Enter Password: "))
        except Exception as e:
            print(e)

