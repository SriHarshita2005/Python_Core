# Create: • Base Account → withdraw() • Subclass SavingsAccount → modifies withdraw() •
# Subclass PremiumSavingsAccount → overrides again but calls parent using super() Show how polymorphism works across multiple levels.

class BaseAccount:
    def withdraw(self,amount):
        print(f"Withdraw {amount} from account")
class SavingsAccount(BaseAccount):
    def withdraw(self,amount):
        print(f"Withdraw {amount} from Savings Account")
class PremiumSavingsAccount(SavingsAccount):
    def withdraw(self,amount):
        super().withdraw(amount)
        print(f"Extra benefits applied for ₹{amount}")
a=BaseAccount()
s=SavingsAccount()
p=PremiumSavingsAccount()
a.withdraw(1000)
s.withdraw(2000)
p.withdraw(3000)


