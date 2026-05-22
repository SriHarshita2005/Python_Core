# Q2. Design a class Product that:
# Maintains a base tax rate applicable to all products.
# Each product has a name and base price.
# Has a method to compute final price including tax.
# Can change tax rate for all products using one method.
# Includes a function to check whether a given price is valid or not (non-negative and realistic).
# Demonstrate:
# 1.Creating multiple products.
# 2.Changing the tax rate.
# 3.Showing updated prices and validity checks.

class Product:
    base_tax_rate=5
    def __init__(self,name,base_price):
        self.name=name
        self.base_price=base_price
    def final_price(self):
        tax = self.base_price * Product.base_tax_rate / 100
        return self.base_price + tax
    @classmethod
    def change_tax_rate(cls,new_rate):
        cls.base_tax_rate=new_rate
    @staticmethod
    def valid(price):
        return  price>=0 and price<=1000000
p1 = Product("Laptop", 50000)
p2 = Product("Phone", 20000)
p3 = Product("Watch", -500)
products=[p1,p2,p3]
print("Before tax change:")
for p in products:
    print(p.name,"Valid:",Product.valid(p.base_price),"Final price:",p.final_price())
print("After changes")
Product.change_tax_rate(10)
for p in products:
    print(p.name,"Valid:",Product.valid(p.base_price),"Final price:",p.final_price())
