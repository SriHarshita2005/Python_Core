
#  Decorator With Input (Parameters)
# Create a decorator that works for a function taking a name as input. It should print "Starting..."
# before greeting the user.
# • Function: def greet(name): print("Hello", name)
# • Expected Output:
# o Starting...
# o Hello Ravi
# o Done

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
