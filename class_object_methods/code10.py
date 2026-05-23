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
        if Student.passing_marks>=self.marks:
            return True
        return False
    @classmethod
    def update_marks(cls,new_marks):
        cls.passing_marks=new_marks
    @staticmethod
    def grade_category(marks):
        if marks>=85:
            return "A"
        elif marks>=60:
            return "B"
        else:
            return "C"
s1=Student("Harshita",90)
s2=Student("Ravi",75)
s3=Student("Anitha",40)
for s in [s1,s2,s3]:
    print(f"{s.name} Grade: {Student.grade_category(s.marks)}")
    s.result()
Student.passing_marks=45
for s in [s1,s2,s3]:
    print(f"{s.name} Grade: {Student.grade_category(s.marks)}")
    s.result()

