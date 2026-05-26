#create a bank account with accno,balance:private,pin:private,name:protected and implement withdraw,
# deposit and display methods

class Bank:
    def __init__(self,a,b,p,name):
        self.a=a
        self.__b=b
        self.__p=p
        self._name=name
    def withdraw(self,amount):
        if self.__b<amount:
            print("Insufficient Balance")
        else:
            self.__b=self.__b-amount
            return self.__b
    def deposit(self,amount):
        self.__b=self.__b+amount
        return self.__b
        print("Amount deposited successfully")
    def display(self):
        p=int(input("Enter pin:"))
        if p==self.__p:
            print(f"Account number={self.a}, Balance:{self.__b}, ")
        else:
            print("Enter correct pin")
b1=Bank(1233000,1234,1234,"Harshitha")
b1.withdraw(500)
b1.deposit(100000)
b1.display()





















