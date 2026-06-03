
#use iterators to generate  prime numbers or composite numbers till n

class A:
    def __init__(self,a):
        self.a=a
        self.c=2
    def __iter__(self):
        self.choice=input(("Enter choice(prime/composite):"))
        return self

    def __next__(self):
        while self.c<self.a:
            num=self.c
            self.c+=1
            fc=0
            for i in range(1,num+1):
                if(num%i==0):
                    fc+=1
            if(self.choice == "prime" and fc==2):
                return num
            elif(self.choice == "composite" and fc>2):
                return num
        raise StopIteration
# num=int(input("enter n value"))
# obj=A(num)
# for i in obj:
#     print(i,end=" ")
#
# 1. Write a custom iterator that prints numbers from 1 to N.

class A:
    def __init__(self,a):
        self.a=a
        self.c=1
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            if self.c<=self.a:
                print(self.c)
                self.c+=1
            else:
                raise StopIteration
# a=A(10)
# for i in a:
#     print(i)

# 2. Create an iterator that returns only even numbers from a given list.

class A:
    def __init__(self,a):
        self.a=a
        self.c=0
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            if self.c<len(self.a):
                if self.a[self.c]%2==0:
                    print(self.a[self.c])

                self.c+=1
            else:
                raise StopIteration
a=A([1,2,3,4,5,6])
for i in a:
    print(i)
#3. Implement an iterator that iterates over a string character by character in reverse order.

st="Hello"
it=iter(st[::-1])
for i in range(len(st)):
    print(next(it))

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

# 5. Write a generator that yields digits from an integer one by one.

def gen(n):
    for i in str(n):
        yield int(i)
n=12345
for i in gen(n):
    print(i)

# 6. Create a generator that yields cumulative sum of numbers in a list. Example: [1,2,3] → 1, 3, 6 .
def gen(n):
    s=0
    for i in n:
        s+=i
        yield s
n=[1,2,3]
for i in gen(n):
    print(i)



# Implement a generator that yields vowels from a string.

def gen(n):
    for i in n:
        if i in "aeiouAEIOU":
            yield(i)
n="Hello"
for i in gen(n):
    print(i)

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
                print(self.word[self.index])
                self.index+=1
            else:
                raise StopIteration
a = "Python is easy to learn"
obj = A(a)
for i in obj:
    print(i)


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

# 10. Implement a generator that yields running maximum from a list Example: [3,1,4,2] → 3, 3, 4, 4

def gen(nums):
    m = 0
    for i in nums:
        if i > m:
            m = i
        yield m
nums = [3, 1, 4, 2]
for i in gen(nums):
     print(i)
# g = gen(nums)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
