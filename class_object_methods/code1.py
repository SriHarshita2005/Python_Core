#Create a class Student with instance attributes name and marks.
# Add an instance method is_passed() that returns True if marks > 40.
# Then create 2 student objects and print whether each has passed or failed.

class Student:
    def __init__ (self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        if (self.marks>40):
            return True

s1=Student("Harshita",50)
s2=Student("Sweety",30)
for s in [s1,s2]:
    if s.is_passed():
        print(f"{s.name} has passed")
    else:
        print(f"{s.name} has failed")
