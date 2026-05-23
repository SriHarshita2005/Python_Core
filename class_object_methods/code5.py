
# Create a class Temperature with:
# instance attribute celsius
# a static method to_fahrenheit(celsius)
# an instance method show_conversion() that uses the static method to print both values.
#
class Temperature:
    def __init__(self,celcius):
        self.celcius=celcius
    @staticmethod
    def to_fahrenheit(celcius):
        fahrenheit=(celcius*9/5)+32
        return fahrenheit
    def show_conversion(self):
        print(f"Celcius :{self.celcius}")
        f=Temperature.to_fahrenheit(self.celcius)
        print(f"Fahrenheit: {f}")
obj=Temperature(32)
obj.show_conversion()