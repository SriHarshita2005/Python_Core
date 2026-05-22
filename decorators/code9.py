

# Negative Result Blocker
# Create a decorator for a subtraction function. If the final result is a negative number, the
# decorator should return 0 instead.
# • Expected Output: (If result is -5) 0

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
