# Decorator to validate input type

def validate_string(func):

    def wrapper(arg):
        if not isinstance(arg, str):
            print("Error: Invalid Input Type")
        else:
            func(arg)

    return wrapper


@validate_string
def display_name(name):
    print("Name:", name)


# Function calls
display_name("Harshita")
display_name(10)