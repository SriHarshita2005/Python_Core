
# Q8. Create a class Course with:
# class variable total_students
# instance variable student_name
# instance method enroll() → increments total_students
# class method show_total(cls) → prints total students
# static method is_eligible(age) → returns True if age ≥ 18
# Demonstrate enrolling multiple students and show total count.

class Course:
    total_students=0
    def __init__(self,student_name):
        self.student_name=student_name

    def enroll(self):
        Course.total_students+=1
        print("Student enrolled successfully")
    @classmethod
    def show_total(cls):
        print(cls.total_students)
    @staticmethod
    def is_eligible(age):
        return age>=18
s1=Course("Harshita")
s2=Course("Ravi")
s1.enroll()
s1.show_total()
s2.enroll()
s2.show_total()
print(s1.is_eligible(10))


