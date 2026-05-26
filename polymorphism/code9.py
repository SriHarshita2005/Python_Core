#Create a function draw(shape) that works for objects of classes Circle, Square, and Rectangle,
# each implementing a draw() method. Add another unrelated class Car with draw() and pass it — what happens and why?

class Circle:
    def draw(self):
        print("Drawing Circle")
class Square:
    def draw(self):
        print("Drawing Square")
class Rectangle:
    def draw(self):
        print("Drawing Rectangle")
class Car:
    def draw(self):
        print("Drawing Car")
def draw(shape):
    shape.draw()
c=Circle()
s=Square()
r=Rectangle()
car=Car()
draw(c)
draw(s)
draw(r)
draw(car)