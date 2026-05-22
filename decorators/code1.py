
# Add Before & After Messages
# Create a decorator that prints "Start" before the function execution and "End" after it finishes.
# • Expected Output:
# o Start
# o Hello
# o End

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
