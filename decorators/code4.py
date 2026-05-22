
# Admin Access Check
# Create a decorator that checks a user_role variable. If the role is not "admin", it should print
# "Access Denied" and prevent the function from running.
# • Expected Output: Access Denied (if user is a 'student').

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

