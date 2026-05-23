

# 9. Write an iterator that returns characters at even indices of a string.

class A:
    def __init__(self, s):
        self.s = s
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.s):
            ch = self.s[self.index]
            self.index += 2
            return ch
        else:
            raise StopIteration
obj = A("Python")
for i in obj:
    print(i)