#Create a Product class where: • price cannot be negative • discount cannot exceed 70% •
# internal final price calculation should not be directly exposed Provide only one public method get_final_price().

class Product:
    def __init__(self,price, discount):
        self.price=price
        self.discount=discount
        if self.price<0:
            print("price cannot be negative")
        if self.discount > 70:
            print("Discount cannot exceed 70 percentage")
    def get_final_price(self):
        final_price=self.price-self.discount
        return final_price
p1 = Product(1000, 20)
print("Final Price:", p1.get_final_price())




