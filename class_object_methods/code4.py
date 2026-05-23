
# Create a class Car with:
# instance attribute mileage
# class attribute wheels = 4
# Add an instance method display_specs() that prints mileage and wheels.
# Then change wheels using a class method, and print again.
#
class Car:
    wheels=4
    def __init__(self,mileage):
        self.mileage=mileage
    def display_specs(self):
        print(f"Mileage:{self.mileage} , Wheels:{Car.wheels}")
    @classmethod
    def change_wheels(cls,new_wheels):
        cls.wheels=new_wheels
c1=Car(10)
c2=Car(20)
print("Before change:")
c1.display_specs()
c2.display_specs()
print("After change:")
Car.wheels=6
c1.display_specs()
c2.display_specs()
