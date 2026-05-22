

# Result Doubler
# Create a decorator that captures the value returned by a function and multiplies it by 2 before
# returning it.
# • Example: If the function returns 25, the final output should be 50.

def my_dec(func):
    def inner(*args,**kwargs):
        result=func(*args,**kwargs)
        return result*2

    return inner
@my_dec
def fun(x):
    return x
print(fun(25))
