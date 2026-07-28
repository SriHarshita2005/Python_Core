#Q6. Design: • Base class Payment with process(amount) • Subclass CreditCardPayment adds
# process(amount, card_type) Demonstrate what happens when overriding with different signatures and how
# Python handles it.

class Payment:
    def process(self,amount):
        print(f"Processing amount:{amount}")
class CreditCardPayment(Payment):
    def process(self,amount,card_type):
        print(f"Amount:{amount} , Card_type:{card_type}")
p=Payment()
p.process(3000)
cc=CreditCardPayment()
cc.process(1000,'Axis')
