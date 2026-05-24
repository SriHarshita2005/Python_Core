
# Q8. Create a HotelRoom class that:
# Keeps a base price per night (shared).
# Each room has room_number, nights_booked, and guest_name.
# Has a method to calculate total bill.
# Allows updating the base price across all rooms.
# Provides a static utility to check if a number of nights is valid (e.g., positive integer only).
# Demonstrate:
# 1.Creating rooms and bookings.
# 2.Changing base price.
# 3.Checking bill updates and validation.

class HotelRoom:
    base_price=1000
    def __init__(self,rn,nb,gn):
        self.rn=rn
        self.nb=nb
        self.gn=gn
    def total_bill(self):
        return self.nb*HotelRoom.base_price
    @classmethod
    def update(cls,new_price):
        cls.base_price=new_price
    @staticmethod
    def check(nights):
        return nights>0 and nights==int(nights)
h1=HotelRoom(101,2,"Harshita")
h2=HotelRoom(102,3,"Ravi")
for h in [h1,h2]:
    print(h.total_bill())
HotelRoom.base_price=900
for h in [h1,h2]:
    print(h.total_bill())
print(HotelRoom.check(10))
print(HotelRoom.check(-5))
print(HotelRoom.check(2.5))





