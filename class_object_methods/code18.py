
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
    base_price = 2000   # price per night

    def __init__(self, room_number, nights_booked, guest_name):
        self.room_number = room_number
        self.nights_booked = nights_booked
        self.guest_name = guest_name

    # instance method
    def total_bill(self):
        return self.nights_booked * HotelRoom.base_price

    # class method
    @classmethod
    def update_price(cls, new_price):
        cls.base_price = new_price
        print("Base price updated to:", cls.base_price)

    # static method
    @staticmethod
    def valid_nights(nights):
        return isinstance(nights, int) and nights > 0
1. Creating rooms and bookings
r1 = HotelRoom(101, 3, "Harshita")
r2 = HotelRoom(102, 5, "Ravi")

rooms = [r1, r2]

print("Before price update:")
for r in rooms:
    print(r.guest_name,
          "| Room:", r.room_number,
          "| Valid Nights:", HotelRoom.valid_nights(r.nights_booked),
          "| Total Bill:", r.total_bill())

# 2. Changing base price
HotelRoom.update_price(3000)

# 3. Updated bills and validation
print("\nAfter price update:")
for r in rooms:
    print(r.guest_name,
          "| Room:", r.room_number,
          "| Valid Nights:", HotelRoom.valid_nights(r.nights_booked),
          "| Total Bill:", r.total_bill())
