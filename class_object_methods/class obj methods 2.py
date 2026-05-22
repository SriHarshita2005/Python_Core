# # Q1. Create a class Student that:
# # Keeps track of the total number of students created.
# # Determines whether a student passed or failed based on a shared passing mark.
# # Provides a method to curve marks by increasing everyone’s marks by a percentage.
# # Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).
# # Demonstrate:
# # 1.Creating multiple students.
# # 2.Applying a grading curve.
# # 3.Displaying updated results with letter grades.
#
# class Student:
#     total_students = 0
#     passing_marks = 40
#
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         Student.total_students += 1
#
#     def result(self):
#         if self.marks >= Student.passing_marks:
#             return "Pass"
#         else:
#             return "Fail"
#
#     @classmethod
#     def apply_curve(cls, students, percent):
#         for s in students:
#             s.marks += s.marks * percent / 100
#
#     @staticmethod
#     def convert(marks):
#         if marks >= 75:
#             return "A"
#         elif marks >= 50:
#             return "B"
#         else:
#             return "C"
#
#
# # Creating students
# s1 = Student("Harshita", 80)
# s2 = Student("Sweety", 40)
# s3 = Student("Ravi", 70)
# s4 = Student("Anitha", 20)
#
# students = [s1, s2, s3, s4]
#
# print("Before Curve:")
# for s in students:
#     print(s.name, s.marks, Student.convert(s.marks), s.result())
#
# # Apply curve
# Student.apply_curve(students, 10)
#
# print("\nAfter Curve:")
# for s in students:
#     print(s.name, round(s.marks, 2), Student.convert(s.marks), s.result())
#
# print("\nTotal Students:", Student.total_students)

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

# class Product:
#     base_tax_rate=5
#     def __init__(self,name,base_price):
#         self.name=name
#         self.base_price=base_price
#     def final_price(self):
#         tax = self.base_price * Product.base_tax_rate / 100
#         return self.base_price + tax
#     @classmethod
#     def change_tax_rate(cls,new_rate):
#         cls.base_tax_rate=new_rate
#     @staticmethod
#     def valid(price):
#         return  price>=0 and price<=1000000
# p1 = Product("Laptop", 50000)
# p2 = Product("Phone", 20000)
# p3 = Product("Watch", -500)
# products=[p1,p2,p3]
# print("Before tax change:")
# for p in products:
#     print(p.name,"Valid:",Product.valid(p.base_price),"Final price:",p.final_price())
# print("After changes")
# Product.change_tax_rate(10)
# for p in products:
#     print(p.name,"Valid:",Product.valid(p.base_price),"Final price:",p.final_price())

# Create an Employee class that:
# Keeps a minimum experience required for promotion (shared across all employees).
# Stores employee name, experience, and department.
# Has a method to check eligibility for promotion.
# Provides a function to update promotion criteria globally.
# Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
# Demonstrate:
# 1.Creating employees from different departments.
# 2.Changing promotion criteria.
# 3.Displaying eligibility results and department validation.

# class Employee:
#     min_experience=3
#     def __init__(self,name,experience,dept):
#         self.name=name
#         self.experience=experience
#         self.dept=dept
#     def check_eligibility(self):
#         if self.experience>=Employee.min_experience:
#             return "Eligible"
#         else:
#             return "Not eligible"
#     @classmethod
#     def update(cls,new_exp):
#         cls.min_experience=new_exp
#         print("Minimum experience updated to:",cls.min_experience)
#     @staticmethod
#     def valid_department(dept):
#         return dept in["HR","Tech","Admin"]
# e1 = Employee("Harshita", 4, "Tech")
# e2 = Employee("Ravi", 2, "HR")
# e3 = Employee("Anitha", 5, "Finance")
# employees=[e1,e2,e3]
# print("Before promotion")
# for e in employees:
#     print(e.name,Employee.valid_department(e.dept),e.check_eligibility())
# Employee.update(5)
#
# print("\nAfter updating criteria:")
#
# for e in employees:
#     print(e.name,Employee.valid_department(e.dept),e.check_eligibility())

#  Build a Loan class that:
# Has a common interest rate for all loans.
# Each object stores borrower name and principal.
# Calculates total payable amount.
# Provides a function to update the interest rate.
# Provides a static function to check loan eligibility (e.g., salary > certain threshold).
# Demonstrate:
# 1.Creating multiple loan accounts.
# 2.Updating interest rates.
# 3.Checking eligibility and total repayment for borrowers.

# class Loan:
#     interest_rate=5
#     def __init__(self,name,principal):
#         self.name=name
#         self.principal=principal
#     def payable_amount(self):
#         return self.principal*Loan.interest_rate
#     @classmethod
#     def update(cls,new_rate):
#         cls.interest_rate=new_rate
#         print("Interest rate updated to:", cls.interest_rate)
#     @staticmethod
#     def is_eligible(salary):
#         return salary>20000
# l1 = Loan("Harshita", 100000)
# l2 = Loan("Ravi", 50000)
# print("Before updating")
# print("Harshita eligible?", Loan.is_eligible(30000))
# print("Ravi eligible?", Loan.is_eligible(15000))
# Loan.update(10)
# print("After updating")
# print(l1.name, "Payable:", l1.payable_amount())
# print(l2.name, "Payable:", l2.payable_amount())

# Create a class Course that:
# Tracks total courses created.
# Each course has a title, duration, and enrolled_students.
# Provides a method to enroll a new student.
# Allows updating the minimum duration for a valid course across all instances.
# Has a static function to check if a given duration is realistic (not negative, not too large).
# Demonstrate:
# 1.Creating multiple courses.
# 2.Enrolling students.
# 3.Updating minimum duration and checking durations.

# class Course:
#     total_courses=0
#     def __init__(self,title,duration,enrolled_students):
#         self.title=title
#         self.duration=duration
#         self.enrolled_students=enrolled_students
#         Course.total_courses+=1
#     def enroll(self):
#         self.enrolled_students+=1
#
#     @classmethod
#     def update_min_duration(cls, new_duration):
#         cls.min_duration = new_duration
#         print("Minimum duration updated to:", cls.min_duration)
#
#     @staticmethod
#     def valid_duration(duration):
#         return duration > 0 and duration <= 100
# c1 = Course("Python", 30, 10)
# c2 = Course("Java", 40, 5)
# c3 = Course("C++", -5, 2)   # invalid duration
# courses = [c1, c2, c3]
# c1.enroll()
# c2.enroll()
# print("Before update:")
# for c in courses:
#     print(c.title,
#           "| Duration valid:", Course.valid_duration(c.duration),
#           "| Students:", c.enrolled_students)
# Course.update_min_duration(10)
# print("\nAfter update:")
# for c in courses:
#     print(c.title,
#           "| Duration valid:", Course.valid_duration(c.duration),
#           "| Students:", c.enrolled_students)
# print("\nTotal Courses:", Course.total_courses)

# Design a class Vehicle that:
# Keeps a record of service charge rate common to all vehicles.
# Each vehicle has a model, kilometers_run, and service history.
# Has a function to calculate service charge based on km and rate.
# Provides a method to update the service rate for all vehicles.
# Provides a static tool to check if a vehicle model is eligible for service (not older than 15 years).
# Demonstrate:
# 1.Creating vehicles with different km and models.
# 2.Updating the service rate.
# 3.Showing charges and eligibility checks.

# class Vehicle:
#     service_charge_rate=100
#     def __init__(self,model, kilometers_run,service_history):
#         self.model=model
#         self.kilometers_run=kilometers_run
#         self.service_history=service_history
#
#     def service_charge(self):
#         return self.kilometers_run * Vehicle.service_charge_rate
#     @classmethod
#     def update_rate(cls, new_rate):
#         cls.service_charge_rate = new_rate
#         (print("Service charge rate updated to:", cls.service_charge_rate))
#     @staticmethod
#     def eligible(years_old):
#         return years_old <= 15
# v1 = Vehicle("Honda City", 10, 2)
# v2 = Vehicle("Swift", 20, 5)
#
# vehicles = [v1, v2]
#
# print("Before updating rate:")
# for v in vehicles:
#     print(v.model,
#           "| Charge:", v.service_charge(),
#           "| Eligible:", Vehicle.eligible(v.service_history))
#
# # update rate
# Vehicle.update_rate(150)
#
# print("\nAfter updating rate:")
# for v in vehicles:
#     print(v.model,
#           "| Charge:", v.service_charge(),
#           "| Eligible:", Vehicle.eligible(v.service_history))

#  Build an Inventory class that:
# Tracks the total number of items across all inventories.
# Each instance maintains its own stock dictionary ({"item": quantity}).
# Provides a method to add or remove stock.
# Allows updating a minimum stock threshold globally.
# Offers a static checker to verify if a stock level is below threshold.
# Demonstrate:
# 1.Managing multiple inventories.
# 2.Adjusting stock threshold.
# 3.Using static validation inside the instance logic.







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

# class HotelRoom:
#     base_price = 2000   # price per night
#
#     def __init__(self, room_number, nights_booked, guest_name):
#         self.room_number = room_number
#         self.nights_booked = nights_booked
#         self.guest_name = guest_name
#
#     # instance method
#     def total_bill(self):
#         return self.nights_booked * HotelRoom.base_price
#
#     # class method
#     @classmethod
#     def update_price(cls, new_price):
#         cls.base_price = new_price
#         print("Base price updated to:", cls.base_price)
#
#     # static method
#     @staticmethod
#     def valid_nights(nights):
#         return isinstance(nights, int) and nights > 0
# 1. Creating rooms and bookings
# r1 = HotelRoom(101, 3, "Harshita")
# r2 = HotelRoom(102, 5, "Ravi")
#
# rooms = [r1, r2]
#
# print("Before price update:")
# for r in rooms:
#     print(r.guest_name,
#           "| Room:", r.room_number,
#           "| Valid Nights:", HotelRoom.valid_nights(r.nights_booked),
#           "| Total Bill:", r.total_bill())
#
# # 2. Changing base price
# HotelRoom.update_price(3000)
#
# # 3. Updated bills and validation
# print("\nAfter price update:")
# for r in rooms:
#     print(r.guest_name,
#           "| Room:", r.room_number,
#           "| Valid Nights:", HotelRoom.valid_nights(r.nights_booked),
#           "| Total Bill:", r.total_bill())


# . Design a LibraryMember class that:
# Tracks total active members.
# Each member has a name and books_borrowed count.
# Has a function to borrow books, with borrowing limit common to all.
# Allows updating borrowing limit globally.
# Has a static function to check if book title is valid (non-empty string, reasonable length).
# Demonstrate:
# 1.Borrowing books for multiple users.
# 2.Changing borrowing limits.
# 3.Validating book titles before borrowing.

class LibraryMember:
    total_members = 0
    borrow_limit = 3

    def __init__(self, name):
        self.name = name
        self.books_borrowed = 0
        LibraryMember.total_members += 1

    # instance method
    def borrow_book(self, title):

        if self.books_borrowed < LibraryMember.borrow_limit:
            self.books_borrowed += 1
            print(self.name, "borrowed", title)
        else:
            print(self.name, "has reached borrowing limit")

    # class method
    @classmethod
    def update_limit(cls, new_limit):
        cls.borrow_limit = new_limit
        print("Borrow limit updated to:", cls.borrow_limit)

    # static method
    @staticmethod
    def valid_title(title):
        return isinstance(title, str) and len(title) > 0 and len(title) <= 50
# 1. Creating members
m1 = LibraryMember("Harshita")
m2 = LibraryMember("Ravi")

# Borrowing books
m1.borrow_book("Python Basics")
m1.borrow_book("Data Science")

m2.borrow_book("AI")
m2.borrow_book("")   # invalid title

print("\nBooks Borrowed:")
print(m1.name, ":", m1.books_borrowed)
print(m2.name, ":", m2.books_borrowed)

# 2. Change borrowing limit
LibraryMember.update_limit(5)

# Borrow more books
m1.borrow_book("Machine Learning")
m1.borrow_book("Deep Learning")

# 3. Validation
print("\nTotal Active Members:", LibraryMember.total_members)


#  Create a class Member that:
# Has a shared BMI limit for “fit” status.
# Each member stores name, height, weight.
# Has a method to calculate BMI and check fit status.
# Provides a function to update BMI limit for all members.
# Offers a tool to check if height and weight entered are valid numbers.
# Demonstrate:
# 1.Creating multiple members.
# 2.Updating BMI standard.
# 3.Displaying fit status and input validity.

class Member:
    bmi_limit = 25

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    # instance method
    def check_fit(self):
        bmi = self.weight / (self.height ** 2)

        if bmi <= Member.bmi_limit:
            status = "Fit"
        else:
            status = "Not Fit"

        return round(bmi, 2), status

    # class method
    @classmethod
    def update_bmi_limit(cls, new_limit):
        cls.bmi_limit = new_limit
        print("BMI limit updated to:", cls.bmi_limit)

    # static method
    @staticmethod
    def valid_input(height, weight):
        return height > 0 and weight > 0
# 1. Creating members
# m1 = Member("Harshita", 1.6, 50)
# m2 = Member("Ravi", 1.7, 80)
#
# members = [m1, m2]
#
# print("Before BMI update:")
# for m in members:
#     bmi, status = m.check_fit()
#
#     print(m.name,
#           "| Valid:", Member.valid_input(m.height, m.weight),
#           "| BMI:", bmi,
#           "| Status:", status)
#
# # 2. Updating BMI limit
# Member.update_bmi_limit(30)
#
# print("\nAfter BMI update:")
# for m in members:
#     bmi, status = m.check_fit()
#
#     print(m.name,
#           "| Valid:", Member.valid_input(m.height, m.weight),
#           "| BMI:", bmi,
#           "| Status:", status)

