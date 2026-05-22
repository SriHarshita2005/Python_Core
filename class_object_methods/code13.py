# Create an Employee class that:
# Keeps a minimum experience required for promotion (shared across all employees).
# Stores employee name, experience, and department.
# Has a method to check eligibility for promotion.
# Provides a function to update promotion criteria globally.
# Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
# Demonstrate:
# 1.Creating employees from different departments.
# 2.Changing promotion criteria.
# 3.Displaying eligibility results and department validation.

class Employee:
    min_experience=3
    def __init__(self,name,experience,dept):
        self.name=name
        self.experience=experience
        self.dept=dept
    def check_eligibility(self):
        if self.experience>=Employee.min_experience:
            return "Eligible"
        else:
            return "Not eligible"
    @classmethod
    def update(cls,new_exp):
        cls.min_experience=new_exp
        print("Minimum experience updated to:",cls.min_experience)
    @staticmethod
    def valid_department(dept):
        return dept in["HR","Tech","Admin"]
e1 = Employee("Harshita", 4, "Tech")
e2 = Employee("Ravi", 2, "HR")
e3 = Employee("Anitha", 5, "Finance")
employees=[e1,e2,e3]
print("Before promotion")
for e in employees:
    print(e.name,Employee.valid_department(e.dept),e.check_eligibility())
Employee.update(5)

print("\nAfter updating criteria:")

for e in employees:
    print(e.name,Employee.valid_department(e.dept),e.check_eligibility())
