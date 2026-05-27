# 4. Write an iterator that yields elements of a list with their index (dont use enumerate)’
class A:
    def __init__(self,a):
        self.a=a
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            if self.index<len(self.a):
                print(self.index , self.a[self.index])
                self.index+=1
            else:
                raise StopIteration
l=[10,20,30,40]
a=A(l)
for i in a:
    print(i)