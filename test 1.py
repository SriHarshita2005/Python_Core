'''
1. Create a decorator for a subtraction function. If the final result is a negative
number, the decorator should return 0 instead.
• Expected Output: (If result is -5) 0

'''

def my_dec(func):
    def inner(*args,**kwargs):
        result=func(*args,**kwargs)
        if(result<0):
            return 0
        return result
    return inner
@my_dec
def subtraction(a,b):
    return a-b
print(subtraction(2,3))

'''
 Create a HotelRoom class that:
• Keeps a base price per night (shared).
• Each room has room_number, nights_booked, and guest_name.
• Has a method to calculate total bill.
• Allows updating the base price across all rooms.
• Provides a static utility to check if a number of nights is valid (e.g.,
positive integer only).
Demonstrate:
1. Creating rooms and bookings.
2. Changing base price.
Checking bill updates and validation

'''
class HotelRoom:
    base_price=1000
    def __init__(self,room_number,nights_booked,guest_name):
        self.room_number = room_number
        self.nights_booked=nights_booked
        self.guest_name=guest_name
    def total_bill(self):
        self.total_bill=HotelRoom.base_price*self.nights_booked
    @classmethod
    def change_price(cls,change_price):
        HotelRoom.base_price=cls.change_price
    @staticmethod
    def is_valid(nights_booked):
        if(h1.nights_booked>0):
            return True
h1=HotelRoom(100,2,"Harshita")
h2=HotelRoom(101,1,"Sweety")
print(h1.total_bill)
h1.change_price(900)
print(h1.total_bill)


'''
Create a class Product with:
• Instance attributes: name, category, price, quantity
• A class variable: total_products
• A constructor __init__() that initializes product details and increments
total_products
• A class method from_string(cls, product_str) that creates an object from
"name-category-price-quantity" format
• A static method is_valid_price(price) that checks if price is greater than 0
Demonstrate:
• Validating price before creating a product
• Using filter() to get products with quantity greater than 10
• Using sorted() to sort products by price 
'''

class Product:
    total_products=0
    def __init__(self,name,category,price,quantity):
        self.name=name
        self.category=category
        self.price=price
        self.quantity=quantity
        Product.total_products+=1
    @classmethod
    def from_strings(cls,product_str):
        cls.p1=Product("abc","ABC",10,-1)
    @staticmethod
    def is_valid(price):
        if price>10:
            return price
        else:
            print("Enter correct price")








