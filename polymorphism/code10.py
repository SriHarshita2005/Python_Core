#Q10. Design a polymorphic system for payment handling (UPI, Card, Cash) — all have a pay() method.
# Now implement a version that checks types explicitly using isinstance() before calling pay().
# Compare both designs and explain why one breaks the spirit of polymorphism.

class UPI:
    def pay(self):
        print("Payment done using UPI")


class Card:
    def pay(self):
        print("Payment done using Card")


class Cash:
    def pay(self):
        print("Payment done using Cash")


def payment(method):

    if isinstance(method, UPI):
        method.pay()

    elif isinstance(method, Card):
        method.pay()

    elif isinstance(method, Cash):
        method.pay()

    else:
        print("Invalid Payment Method")


# Driver Code
u = UPI()
c = Card()
ca = Cash()

payment(u)
payment(c)
payment(ca)