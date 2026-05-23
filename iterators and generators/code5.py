# 5. Write a generator that yields digits from an integer one by one.

def gen(n):
    for i in str(n):
        yield int(i)
n=12345
for i in gen(n):
    print(i)