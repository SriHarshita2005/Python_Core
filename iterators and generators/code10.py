# 10. Implement a generator that yields running maximum from a list Example: [3,1,4,2] → 3, 3, 4, 4
def gen(l):
    m = 0
    for i in l:
        if i > m:
            m = i
        yield m
nums = [3, 1, 4, 2]
g = gen(nums)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
