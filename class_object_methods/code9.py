
class BankAccount:

    # Class variable
    bank_name = "State Bank"

    # Constructor
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    # Static method
    @staticmethod
    def validate_amount(amount):
        return amount > 0

    # Instance method
    def deposit(self, amount):

        # Using static method inside instance method
        if BankAccount.validate_amount(amount):
            self.balance += amount
            print(f"{amount} deposited successfully")
        else:
            print("Invalid deposit amount")

    # Class method
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
        print(f"\nBank name changed to: {cls.bank_name}")

    # Display method
    def display(self):
        print("\nAccount Details")
        print("Bank Name :", BankAccount.bank_name)
        print("Holder Name :", self.holder)
        print("Balance :", self.balance)


# ---------------- DEMONSTRATION ----------------

# Creating objects
# acc1 = BankAccount("Harshita", 5000)
# acc2 = BankAccount("Rahul", 3000)
#
# # Display initial details
# acc1.display()
# acc2.display()
#
# # Transactions
# acc1.deposit(2000)
# acc2.deposit(-500)
#
# # Display updated balances
# acc1.display()
# acc2.display()
#
# # Changing bank name using class method
# BankAccount.change_bank_name("National Bank")
#
# # Updated bank name reflected in all objects
# acc1.display()
# acc2.display()