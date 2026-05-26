#1.  Create a BankAccount class that stores: • account number • balance (should not be directly modifiable)
# You must: 1. Make the balance attribute inaccessible from outside.
# 2. Provide functions to deposit/withdraw that validate the amount.
# 3. Prevent withdrawal if balance becomes negative.
# 4. Show what happens if someone tries to modify balance directly and why encapsulation prevents it.


class BankAccount:
    def __init__(self,acc,balance):
        self.acc=acc
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            print("Amount Deposited")
            self.__balance+=amount
            return self.__balance
        else:
            print("Invalid Amount")
    def withdraw(self,amount):
        if amount<self.__balance:
            print("Amount withdrawed")
            self.__balance=self.__balance-amount
            return self.__balance
        else:
            print("Insufficient balance")
obj=BankAccount(12345,5000)
print(obj.withdraw(2000))
print(obj.deposit(3000))

