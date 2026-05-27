# 10. Implement a generator that yields running maximum from a list Example: [3,1,4,2] → 3, 3, 4, 4
# def gen(l):
#     m = 0
#     for i in l:
#         if i > m:
#             m = i
#         yield m
# nums = [3, 1, 4, 2]
# g = gen(nums)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
def gen(n):
    max=0
    for i in n:
        if i>max:
            max=i
        yield max
n=[1,2,4,3]
for i in gen(n):
    print(i)
