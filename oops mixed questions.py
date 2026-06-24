# Question 1: Item and Book
# Create an abstract base class Item and a concrete subclass Book.
# Requirements:
# Item must require get_summary().
# Book stores:
# title
# private _metadata dictionary
# protected _available flag
# Use properties to safely read metadata.
# Include a shared catalog_tag and a way to update it globally.
# Add a pricing method with default parameter discount=0.
# Implement __str__() and __repr__().
# Add a validator for metadata keys.
# Create books, print str/repr, update shared tag, perform shallow copy and deep copy of the book list, and show differences.

from abc import ABC , abstractmethod
class Item(ABC):
    catalog_tag = "General"
    @classmethod
    def update_catalog_tag(cls,tag):
        cls.catalog_tag = tag
    def get_summary(self):
        pass
class Book(Item):
    def __init__(self,title,metadata,available = True):
        self.title = title
        self._available=available
        for key in metadata:
            self.validate_key(key)
        self.__metadata = metadata
    @property
    def metadata(self):
        return self.__metadata
    @staticmethod
    def validate_key(key):
        if not isinstance(key,str):
            print("Metadata key must be a string")
    def price(self,amount,discount):
        return amount - (discount*amount)/100
    def get_summary(self):
        return f"Book: {self.title}"
    def __str__(self):
        return f"{self.title} , {self._available}"
    def __repr__(self):
        return f"{self.title} , {self._available}"

# b1 = Book("Python Basics", {"author": "John", "pages": 300})
# b2 = Book("OOP Concepts", {"author": "Alice", "pages": 250})
# print(b1)
# print(repr(b1))
# print(b1.get_summary())
# print("Metadata:", b1.metadata)
# print("Catalog Tag:", Book.catalog_tag)
# Book.update_catalog_tag("PROGRAMMING")
# print("Updated Catalog Tag:", Book.catalog_tag)
# print("Price after 10% discount:", b1.price(500, 10))


# Question 2: UserBase and Member
# Build an abstract class UserBase and subclass Member.
# Requirements:
# UserBase must require get_role().
# Member stores:
# username
# protected _credentials
# private _perms list
# user + perm adds permission.
# user - perm removes permission.
# Equality compares identity and permissions.
# Include class-level:
# user_count
# admin_flag
# perform(action, timeout=3).
# Implement __str__() and __repr__() with masked credentials.
# Add a validator for permission names.
# Modify permissions using operators, compare users, and demonstrate shallow copy vs deep copy.

from abc import ABC , abstractmethod
class UserBase(ABC):
    @abstractmethod
    def get_role(self):
        pass
class Member(UserBase):
    user_count = 0
    admin_flag = False
    permission = ["write","read","execute","update","delete","upgrade","degrade"]
    def __init__(self,username,credentials):
        self.username = username
        self._credentials = credentials
        self.__perms = []
        Member.user_count+=1
    def perform(self,action,timeout = 3):
        pass
    def get_role(self):
        pass
    @staticmethod
    def validate(p:str):
        return p.lower() in Member.permission

    def __add__(self, other):
        if other not in self.__perms:
            self.__perms.append(other)
            return self
    def __sub__(self, other):
        if other in self.__perms:
            self.__perms.remove(other)
            return self
        else:
            print("Permission not found")
            return self

    def __eq__(self, other):
        return self.username == other.username and self.__perms == other.__perms

    def __str__(self):
        return f"{self.username}, credentials=****"

    def __repr__(self):
        return f"{self.username} : {self.__perms}"
# m1 = Member("Harshita", "1234")
# m2 = Member("Harshita", "1234")
# m1 + "read"
# m1 + "write"
# m2 + "read"
# m2 + "write"
# print(m1)
# print(repr(m1))
# print(m1 == m2)
# m1 - "write"
# print(repr(m1))
# m1.perform("Upload")
# print("Role:", m1.get_role())
# print("User Count:", Member.user_count)


# Question 3: VehicleBase and Car
# Create an abstract class VehicleBase and subclass Car.
# Requirements:
# VehicleBase requires diagnose().
# Car stores:
# model
# protected _miles
# private _log
# Create a property for miles.
# Create Fleet composition:
# fleet + car registers car
# len(fleet) returns count
# "car in fleet" works
# Shared service_rate affects service cost.
# Implement __str__() and __repr__() with masked logs.
# Add mileage validator.
# Register cars, demonstrate polymorphic diagnose(), and show shallow vs deep copy behavior.

from abc import ABC , abstractmethod
from copy import copy , deepcopy
class VehicleBase(ABC):
    @abstractmethod
    def diagnose(self):
        pass
class Car(VehicleBase):
    service_rate = 10
    def __init__(self,model,miles):
        self.model = model
        self._miles = miles
        self.__log = []
    @property
    def miles(self):
        return self._miles
    @staticmethod
    def validator(miles):
        if miles <0:
            print("Mileage cannot be negative")
        else:
            return True
    def add_log(self, other):
        self.__log.append(other)

    def service_cost(self):
        return self._miles * Car.service_rate

    def diagnose(self):
        return f"{self.model} diagnosed successfully"

    def __str__(self):
        return f"{self.model}, {self._miles} miles, {'*' * len(self.__log)}"

    def __repr__(self):
        return f"{self.model}, {self._miles}, {'*' * len(self.__log)}"
class Fleet:
    def __init__(self):
        self.cars = []
    def __add__(self, other):
        self.cars.append(other)
        return self
    def __len__(self):
        return len(self.cars)
    def __contains__(self, item):
        return item in self.cars
# c1 = Car("BMW", 1000)
# c2 = Car("Audi", 2000)
# c1.add_log("Oil Change")
# c1.add_log("Brake Check")
# c2.add_log("Engine Service")
# fleet = Fleet()
# fleet + c1
# fleet + c2
# print("Fleet Size:", len(fleet))
# print(c1 in fleet)
# print("\nPolymorphism:")
# for car in fleet.cars:
#     print(car.diagnose())
# print("\nString Representation:")
# print(c1)
# print(repr(c1))
# print("\nService Cost:")
# print(c1.service_cost())
# Car.service_rate = 20
# print("Updated Service Cost:", c1.service_cost())
# # Shallow Copy vs Deep Copy
# shallow_fleet = copy(fleet)
# deep_fleet = deepcopy(fleet)
# c1.add_log("Tyre Change")
# print("\nOriginal Fleet:")
# print(fleet.cars)
# print("\nShallow Copy Fleet:")
# print(shallow_fleet.cars)
# print("\nDeep Copy Fleet:")
# print(deep_fleet.cars)

# Question 4: Product and Cart
# Build Product, Cart, and Order.
# Requirements:
# Product stores:
# private _price
# id
# Validate product id.
# Cart stores products privately.
# add(product, qty=1).
# cart + product adds product.
# cart - product removes product.
# len(cart) returns item count.
# Order takes a snapshot:
# shallow copy by default
# optional deep copy
# Implement __str__() and __repr__().
# Shared discount applied globally.
# Add/remove products, create snapshots, mutate cart, and show differences.



# Question 5: Character, Warrior, Mage, and Party
# Create abstract class Character and subclasses Warrior and Mage.
# Requirements:
# Character requires attack(target).
# Store:
# protected _hp
# private _inventory
# hp property prevents negative HP.
# Methods changing HP use default parameter reason='combat'.
# char + item adds inventory item.
# char - item removes inventory item.
# item in char checks inventory.
# Party stores characters privately.
# len(party) returns number of characters.
# Iterating through party calls attack() polymorphically.
# Shared global_buff affects all characters.
# Implement __str__() and __repr__() with masked inventory.
# Add item validator.
# Demonstrate inventory operations, party iteration, shallow vs deep copy, and global buff updates.

from abc import ABC , abstractmethod
from copy import copy , deepcopy
class Character(ABC):
    global_buff = 1
    def __init__(self,hp):
        self._hp = hp
        self.__inventory = []
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self,value):
        if value <0:
            self._hp = 0
        else:
            self._hp = value
    def change_hp(self,amount,reason ="combat"):
        self.hp += amount
        print(f"HP changed because of {reason}")
    @staticmethod
    def validate_item(item):
        return isinstance(item,str)
    def __add__(self, other):
        if Character.validate_item(other):
            self.__inventory.append(other)
        return self
    def __sub__(self, other):
        if other in self.__inventory:
            self.__inventory.remove(other)
        return self

    def __contains__(self, item):
        return item in self.__inventory

    def __str__(self):
        return f"HP={self._hp}, {'*' * len(self.__inventory)}"

    def __repr__(self):
        return f"HP={self._hp}, {'*' * len(self.__inventory)}"

    @abstractmethod
    def attack(self,target):
        pass
class Warrior(Character):
    def attack(self, target):
        print(f"Warrior attacks {target} with {10 * Character.global_buff} power")
class Mage(Character):
    def attack(self, target):
        print(f"Mage attacks {target} with {8 * Character.global_buff} power")
class Party:

    def __init__(self):
        self.__characters = []

    def add_character(self, char):
        self.__characters.append(char)
    def __len__(self):
        return len(self.__characters)
    def __iter__(self):
        return iter(self.__characters)
w = Warrior(100)
m = Mage(80)

# Inventory Operations
w + "Sword"
w + "Shield"

m + "Staff"

print("Sword" in w)     # True

w - "Shield"

print(w)
print(repr(w))

# Party
party = Party()

party.add_character(w)
party.add_character(m)

print("Party Size:", len(party))

# Polymorphism
print("\nAttacks:")
for char in party:
    char.attack("Dragon")

# HP Changes
w.change_hp(-20)
m.change_hp(10, "healing")

print("Warrior HP:", w.hp)
print("Mage HP:", m.hp)

# Global Buff
Character.global_buff = 2

print("\nAfter Global Buff:")
for char in party:
    char.attack("Dragon")

# Shallow Copy vs Deep Copy
shallow_party = copy(party)
deep_party = deepcopy(party)

w + "Potion"

print("\nOriginal Party:")
for char in party:
    print(char)

print("\nShallow Copy Party:")
for char in shallow_party:
    print(char)

print("\nDeep Copy Party:")
for char in deep_party:
    print(char)
