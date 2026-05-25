#Q4. Create a base class Transport with move() and derived classes Bus and Bike that override it but
# also call the parent implementation using super(). Show the combination of reuse + custom behavior.

class Transport:
    def move(self):
        print("Moving")
class Bus(Transport):
    def move(self):
        print("BUS is moving")
        super().move()
class Bike(Transport):
    def move(self):
        print("BIKE is moving")
        super().move()
b1=Bus()
b2=Bike()
b1.move()
b2.move()

