
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
        return (celcius*9/5)+32

    def show_conversion(self):
        print("celcius",self.celcius)
        f=Temperature.to_fahrenheit(self.celcius)
        print("fahrenheit",f)


obj=Temperature(32)
obj.show_conversion()