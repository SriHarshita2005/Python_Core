 #implement a generator that yields vowels from a string.

def gen(n):
    for i in n:
        if i in "AEIOUaeiou":
            yield i
n='Hello'
for i in gen(n):
    print(i)