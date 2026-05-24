#  Create a class Member that:
# Has a shared BMI limit for “fit” status.
# Each member stores name, height, weight.
# Has a method to calculate BMI and check fit status.
# Provides a function to update BMI limit for all members.
# Offers a tool to check if height and weight entered are valid numbers.
# Demonstrate:
# 1.Creating multiple members.
# 2.Updating BMI standard.
# 3.Displaying fit status and input validity.

class Member:
    bmi_limit=25
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
    def check_fit(self):
        bmi= self.weight/(self.height**2)
        if Member.bmi_limit<=bmi:
            return "Fit"
        else:
            return "Not Fit"
    @classmethod
    def update_bmi(cls,new_bmi):
        cls.bmi_limit=new_bmi
    @staticmethod
    def check(height,weight):
        return height>0 and weight>0
m1 = Member("Harshita", 1.6, 50)
m2 = Member("Ravi", 1.7, 80)
for m in [m1,m2]:
    print(m.name , m.check_fit())
Member.bmi_limit=10
for m in [m1,m2]:
    print(m.name , m.check_fit())
for m in [m1,m2]:
    print(m.check(10,-20))


