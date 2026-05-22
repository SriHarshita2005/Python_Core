
# Create a decorator that takes a string returned by a function and converts the entire string to
# uppercase.
# • Function: def get_msg(): return "hello world"
# • Expected Output: HELLO WORLD

def my_dec(func):
    def inner(*args,**kwargs):

        return func(*args,**kwargs).upper()
    return inner
@my_dec
def convert():
    return "hello world"
print(convert())
