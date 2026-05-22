# #
#  Create a class Student with:
# class variable passing_marks = 40
# instance attributes name, marks
# instance method result() → prints pass/fail using class variable
# class method update_passing_marks(cls, new_marks)
# static method grade_category(marks) → returns "A", "B", "C" based on score ranges
# Use all three in a program that:
# 1.Creates students
# 2.Updates the passing criteria
# Displays grade category and result

class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>=Student.passing_marks:
            print("pass")
        else:
            print("fail")
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.passing_marks=new_marks
    @staticmethod
    def grade_category(marks):
        if marks>=75:
            return "A"
        elif( marks>=50):
            return "B"
        else:
            return "C"
s1 = Student("Harshita", 82)
s2 = Student("Sweety", 55)
s3 = Student("Ravi", 38)
print("Before updating")
for s in [s1,s2,s3]:
    print(f"{s.name} Grade: {Student.grade_category(s.marks)}")
    s.result()
Student.update_passing_marks(45)
print("After updating")
for s in [s1,s2,s3]:
    print(f"{s.name} Grade: {Student.grade_category(s.marks)}")
    s.result()