
# 8. Create an iterator that yields words from a sentence one by one.

class A:
    def __init__(self,a):
        self.word=a.split()
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            if self.index<len(self.word):
                print (self.word[self.index])
                self.index+=1
            else:
                raise StopIteration
a=A("Python is love")
for i in a :
    print(i)