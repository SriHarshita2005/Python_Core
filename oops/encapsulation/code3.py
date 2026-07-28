#3. Create a SecureFile class that: • stores content privately • provides a method read(password) •
# refuses access if the password is incorrect •
# logs an "Unauthorized attempt" internally (cannot be accessed from outside)

class SecureFile:
    def __init__(self,content,password):
        self.__content=content
        self.__password=password
        self.__log=[]
    def read(self,password):
        if password==self.__password:
            return self.__content
        else:
            self.__log.append("Unauthorized attempt")
            print("Access Denied")
obj = SecureFile("Python Notes", "1234")
print(obj.read("1234"))
print(obj.read("0000"))