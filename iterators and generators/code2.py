# 2. Create an iterator that returns only even numbers from a given list.

class A:
    def __init__(self,a):
        self.a=a
        self.c=0
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            if self.c<=len(self.a):
                if self.a[self.c]%2==0:
                    value=self.a[self.c]
                    print( value)
                self.c+=1
            else:
                raise StopIteration
a=A([1,2,3,4,5,6,1,2,3,4])
for i in a:
    print(i)