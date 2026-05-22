'''
def my_decorator(func):
    def inner():
        print("Before Function")
        func()
        print("After Function")
    return inner
@my_decorator
def greet():
    print("Hello")
greet()


def greet(func):
    def inner(*args,**kwargs):
        print("The number is even or odd")
        func(*args,**kwargs)
    return inner
@greet
def is_even(n):
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")
is_even(25)

'''

'''
Add Before & After Messages
Create a decorator that prints "Start" before the function execution and "End" after it finishes.
• Expected Output:
o Start
o Hello
o End

def my_dec(func):
    def inner():
        print("Start")
        func()
        print("End")
    return inner
@my_dec
def greet():
    print("Hello")
greet()
'''

'''
 Decorator With Input (Parameters)
Create a decorator that works for a function taking a name as input. It should print "Starting..."
before greeting the user.
• Function: def greet(name): print("Hello", name)
• Expected Output:
o Starting...
o Hello Ravi
o Done

def my_dec(func):
    def inner(*args,**kwargs):
        print("Starting...")
        func(*args,**kwargs)
        print("Done")
    return inner
@my_dec
def greet(name):
    print(f"Hello {name}")
greet("Ravi")
'''

'''
Result Doubler
Create a decorator that captures the value returned by a function and multiplies it by 2 before
returning it.
• Example: If the function returns 25, the final output should be 50.

def my_dec(func):
    def inner(*args,**kwargs):
        result=func(*args,**kwargs)
        return result*2

    return inner
@my_dec
def fun(x):
    return x
print(fun(25))
'''
'''
Admin Access Check
Create a decorator that checks a user_role variable. If the role is not "admin", it should print
"Access Denied" and prevent the function from running.
• Expected Output: Access Denied (if user is a 'student').
'''
'''
user_role="student"
def my_dec(func):
    def inner():
        if user_role!="admin":
            print("Access Denied")
        return func
    return inner()
@my_dec
def check_access():
    print("Welcome")
check_access()
'''

'''
Create a decorator that takes a string returned by a function and converts the entire string to
uppercase.
• Function: def get_msg(): return "hello world"
• Expected Output: HELLO WORLD
'''
def my_dec(func):
    def inner(*args,**kwargs):

        return func(*args,**kwargs).upper()
    return inner
@my_dec
def convert():
    return "hello world"
print(convert())

'''
Call Counter
Create a decorator that tracks how many times a function has been called. It should print the
count every time the function is executed.
• Expected Output: * Called 1 time
o Called 2 times
'''





'''
Prefix ID Decorator
Create a decorator that adds the prefix "ID: " to any name returned by a function.
• Function: def get_name(): return "Ravi"
• Expected Output: ID: Ravi


def my_dec(func):
    def inner():
        name=func()
        return "ID: "+name
    return inner
@my_dec
def get_name():
    return "Ravi"
print(get_name())

'''

'''
The Double Message Wrapper
Create a decorator that prints "Initializing..." before the function starts and "Cleanup Complete"
immediately after it finishes.
• Expected Output: * Initializing...
o [Function Logic Runs]
o Cleanup Complete

def my_dec(func):
    def inner():
        print("Initilializing.....")
        func()
        print("Cleanup Complete")
    return inner()
@my_dec
def message_wrapper():
    print("Function running")
message_wrapper()
'''

'''  
Negative Result Blocker
Create a decorator for a subtraction function. If the final result is a negative number, the
decorator should return 0 instead.
• Expected Output: (If result is -5) 0

def my_dec(func):
    def inner(*args,**kwargs):
        result=func(*args,**kwargs)
        if result<0:
            return 0
        return result
    return inner
@my_dec
def subtract(a,b):
    return a-b
print(subtract(3,1))
'''

'''
Input Type Validator
Create a decorator that checks the argument of a function. If the argument is not a string, it
should print "Error: Invalid Input Type" and not execute the function.
• Expected Output: Error: Invalid Input Type (if an integer is passed).
'''




