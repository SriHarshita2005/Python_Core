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
    bmi_limit = 25

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    # instance method
    def check_fit(self):
        bmi = self.weight / (self.height ** 2)

        if bmi <= Member.bmi_limit:
            status = "Fit"
        else:
            status = "Not Fit"

        return round(bmi, 2), status

    # class method
    @classmethod
    def update_bmi_limit(cls, new_limit):
        cls.bmi_limit = new_limit
        print("BMI limit updated to:", cls.bmi_limit)

    # static method
    @staticmethod
    def valid_input(height, weight):
        return height > 0 and weight > 0
# 1. Creating members
# m1 = Member("Harshita", 1.6, 50)
# m2 = Member("Ravi", 1.7, 80)
#
# members = [m1, m2]
#
# print("Before BMI update:")
# for m in members:
#     bmi, status = m.check_fit()
#
#     print(m.name,
#           "| Valid:", Member.valid_input(m.height, m.weight),
#           "| BMI:", bmi,
#           "| Status:", status)
#
# # 2. Updating BMI limit
# Member.update_bmi_limit(30)
#
# print("\nAfter BMI update:")
# for m in members:
#     bmi, status = m.check_fit()
#
#     print(m.name,
#           "| Valid:", Member.valid_input(m.height, m.weight),
#           "| BMI:", bmi,
#           "| Status:", status)
