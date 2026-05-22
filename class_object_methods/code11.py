# # Q1. Create a class Student that:
# # Keeps track of the total number of students created.
# # Determines whether a student passed or failed based on a shared passing mark.
# # Provides a method to curve marks by increasing everyone’s marks by a percentage.
# # Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).
# # Demonstrate:
# # 1.Creating multiple students.
# # 2.Applying a grading curve.
# # 3.Displaying updated results with letter grades.

class Student:
    total_students = 0
    passing_marks = 40

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.total_students += 1

    def result(self):
        if self.marks >= Student.passing_marks:
            return "Pass"
        else:
            return "Fail"

    @classmethod
    def apply_curve(cls, students, percent):
        for s in students:
            s.marks += s.marks * percent / 100

    @staticmethod
    def convert(marks):
        if marks >= 75:
            return "A"
        elif marks >= 50:
            return "B"
        else:
            return "C"


# Creating students
s1 = Student("Harshita", 80)
s2 = Student("Sweety", 40)
s3 = Student("Ravi", 70)
s4 = Student("Anitha", 20)

students = [s1, s2, s3, s4]

print("Before Curve:")
for s in students:
    print(s.name, s.marks, Student.convert(s.marks), s.result())

# Apply curve
Student.apply_curve(students, 10)

print("\nAfter Curve:")
for s in students:
    print(s.name, round(s.marks, 2), Student.convert(s.marks), s.result())

print("\nTotal Students:", Student.total_students)
