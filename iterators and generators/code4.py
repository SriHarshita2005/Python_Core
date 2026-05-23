# 4. Write an iterator that yields elements of a list with their index (dont use enumerate)’

class A:
    def __init__(self,a):
        self.a=a
        self.c=0
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            if self.c<len(self.a):
                print (self.c, self.a[self.c])
                self.c+=1
            else:
                raise StopIteration
l = [10, 20, 30, 40]
obj = A(l)
for i in obj:
    print(i)