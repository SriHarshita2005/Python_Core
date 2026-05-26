#.Design an Employee class where: • salary is hidden • outsiders cannot read salary directly •
# use getter method that logs each access attempt • provide a method to update salary but only if the
# new salary is higher (prevent accidental downgrade)

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
        self.__log=[]
    def get_salary(self):
        self.__log.append("Salary Accessed")
        return self.__salary
    def update_salary(self,new_salary):
        if new_salary>self.__salary:
            self.__salary=new_salary
            print("Salary Updated")
        else:
            print("Salary must be higher")
obj = Employee("Harshita", 50000)
print(obj.get_salary())
obj.update_salary(60000)
print(obj.get_salary())
obj.update_salary(30000)