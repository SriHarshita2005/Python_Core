 #Create a class Employee with attributes name and company_name = "TechCorp".
# Add a class method change_company(cls, new_name) to update the company name for all employees.
# Demonstrate how this change affects all instances.
#
class Employee:
    company_name="TechCorp"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
e1=Employee("Harshita")
e2=Employee("Ravi")
for e in [e1,e2]:
    print(f"{e1.company_name},{e.name}")
Employee.company_name="CVCORP"
for e in [e1,e2]:
    print(f"{e1.company_name},{e.name}")
