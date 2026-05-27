# 1. Write a custom iterator that prints numbers from 1 to N.

class A:
    def __init__(self,a):
        self.c=0
        self.a=a
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            if self.c<self.a:
                self.c+=1
                print(self.c)
            else:
                raise StopIteration
a=A(10)
for i in a:
    print(i)
