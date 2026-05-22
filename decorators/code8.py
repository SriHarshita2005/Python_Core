
#
# The Double Message Wrapper
# Create a decorator that prints "Initializing..." before the function starts and "Cleanup Complete"
# immediately after it finishes.
# • Expected Output: * Initializing...
# o [Function Logic Runs]
# o Cleanup Complete

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
