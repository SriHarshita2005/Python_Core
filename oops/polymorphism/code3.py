#Create a Vector class that supports: • + operator → add coordinates • == operator → compare equality
# Show how operator overiding gives natural polymorphism to user-defined classes.

class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self, other):
        return self.a+other.a, self.b+other.b
    def __eq__(self, other):
        return self.a==other.a,self.b==other.b
    def __str__(self):
        return (f"A:{self.a} , B:{self.b}")
v1=Vector(10,20)
v2=Vector(20,30)
print(v1)
print(v1+v2)
print(v1==v2)

