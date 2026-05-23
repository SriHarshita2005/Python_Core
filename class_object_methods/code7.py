#
# Create a class Employee with:
# instance attributes: name, base_salary
# class variable: bonus_rate = 0.1
# instance method: final_salary() → base_salary + (base_salary × bonus_rate)
# class method: update_bonus(cls, new_rate) → updates bonus for all employees
# static method: is_valid_salary(sal) → checks if salary > 0
# Create two employees, show final salaries, update bonus rate, and show again.
#
class Employee:
    bonus_rate=0.1
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def final_salary(self):
        return self.base_salary+(self.base_salary*Employee.bonus_rate)
    @classmethod
    def update_bonus(cls,new_rate):
        cls.bonus_rate=new_rate
        print("Bonus rate updated")
    @staticmethod
    def is_valid_salary(sal):
        return sal>0
e1=Employee("Harshita",20000)
e2=Employee("Ravi",10000)
print(e1.final_salary())
print(e2.final_salary())
Employee.bonus_rate=0.5
print(e1.final_salary())
print(e2.final_salary())
print(e1.is_valid_salary(-10000))