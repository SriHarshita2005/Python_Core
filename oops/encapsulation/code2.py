#2. Design a Student class where marks: • should always be between 0 and 100 •
# should never be set directly Enable updating marks only through a controlled method that performs range checks.
# Demonstrate: • trying to assign marks manually • why encapsulation protects invalid states

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks
    def set_marks(self,marks):
        if marks>=0 and marks<=100:
            self.__marks=marks
            print("Marks Updated")
        else:
            print("Invalid Marks")
    def get_marks(self):
        return self.__marks
s1=Student("Harshita",70)
print(s1.get_marks())
s1.set_marks(95)
print(s1.get_marks())
s1.set_marks(150)

# s1.set_marks(-45)
# print(s1.get_marks())

