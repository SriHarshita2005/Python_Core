
# . Create a class BankAccount with:
# class variable bank_name
# instance variables holder and balance
# instance method deposit(amount)
# class method change_bank_name(cls, new_name)
# static method validate_amount(amount) → returns True if amount > 0
# Show transactions and how static + class methods work together.

class BankAccount:
    bank_name="Axis Bank"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amount):
        if self.balance>0:
            self.balance+=amount
            return self.balance
        else:
            return "Negative balance not allowed"
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
    @staticmethod
    def validate_amount(amount):
        return amount>0

b1=BankAccount("Harshita",10000)
b2=BankAccount("Ravi", -20000)
b1.deposit(1000)
b2.deposit(-500)
print(b1.balance)
print(b2.balance)
BankAccount.bank_name="State Bank"
print(b2.validate_amount(-20000))



