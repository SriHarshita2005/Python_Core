

# Prefix ID Decorator
# Create a decorator that adds the prefix "ID: " to any name returned by a function.
# • Function: def get_name(): return "Ravi"
# • Expected Output: ID: Ravi


def my_dec(func):
    def inner():
        name=func()
        return "ID: "+name
    return inner
@my_dec
def get_name():
    return "Ravi"
print(get_name())

