# 3. Implement an iterator that iterates over a string character by character in reverse order.

st="Hello"
it=iter(st[::-1])
for i in range(len(st)):
    print(next(it))