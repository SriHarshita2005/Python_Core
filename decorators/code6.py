
# Call Counter
# Create a decorator that tracks how many times a function has been called. It should print the
# count every time the function is executed.
# • Expected Output: * Called 1 time
# o Called 2 times

# Decorator to count function calls

def call_counter(func):
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        print(f"Called {count} time")
        func()

    return wrapper


@call_counter
def greet():
    print("Hello")


# Function calls
greet()
greet()





