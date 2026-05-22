#  Build a Loan class that:
# Has a common interest rate for all loans.
# Each object stores borrower name and principal.
# Calculates total payable amount.
# Provides a function to update the interest rate.
# Provides a static function to check loan eligibility (e.g., salary > certain threshold).
# Demonstrate:
# 1.Creating multiple loan accounts.
# 2.Updating interest rates.
# 3.Checking eligibility and total repayment for borrowers.

class Loan:
    interest_rate=5
    def __init__(self,name,principal):
        self.name=name
        self.principal=principal
    def payable_amount(self):
        return self.principal*Loan.interest_rate
    @classmethod
    def update(cls,new_rate):
        cls.interest_rate=new_rate
        print("Interest rate updated to:", cls.interest_rate)
    @staticmethod
    def is_eligible(salary):
        return salary>20000
l1 = Loan("Harshita", 100000)
l2 = Loan("Ravi", 50000)
print("Before updating")
print("Harshita eligible?", Loan.is_eligible(30000))
print("Ravi eligible?", Loan.is_eligible(15000))
Loan.update(10)
print("After updating")
print(l1.name, "Payable:", l1.payable_amount())
print(l2.name, "Payable:", l2.payable_amount())
