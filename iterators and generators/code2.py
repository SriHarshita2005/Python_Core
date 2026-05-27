# 2. Create an iterator that returns only even numbers from a given list.
class A:
    def __init__(self,a):
        self.a=a
        self.c=-1
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            self.c+=1
            if self.c<len(self.a):
                if self.a[self.c]%2==0:
                    return self.a[self.c]
            else:
                raise StopIteration
a=A([2,3,4,5,3,2,1])
for i in a:
    print (i)

#print(list(a))

