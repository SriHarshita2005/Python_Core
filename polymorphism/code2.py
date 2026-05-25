#Q2. Write a function operate(device) that calls device.start().
# Pass in objects of Car, Computer, and WashingMachine — all of which define a start() method,
# but share no inheritance relationship. Show that Python’s polymorphism works through behavior, not type.

class Car:
    def start(self):
        print("Car")
class Computer:
    def start(self):
        print("Computer")
class Washing_Machine:
    def start(self):
        print("Washing Machine")
def operate(device):
    device.start()
l=[Car(),Computer(),Washing_Machine()]
for i in l:
    operate(i)
