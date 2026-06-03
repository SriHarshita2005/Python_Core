# * * * *
# * * * *
# * * * *
# * * * *

n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*" , end=" ")
    print()
# *
# * *
# * * *
n=3
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
# * * *
# * *
# *
n=3
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
# *
# **
# ***
# ****
n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
# ****
# ***
# **
# *
n=4
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()
# 1 1 1
# 1 1 1
# 1 1 1
n=3
for i in range(1,n+1):
    for j in range(1,n+1):
        print("1",end=" ")
    print()
# 1
# 1 2
# 1 2 3
n=3
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
# 1
# 2 2
# 3 3 3
n=3
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
# 1 2 3
# 1 2
# 1
n=3
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
# 1
# 2 3
# 4 5 6
n=3
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()
# A
# A B
# A B C
num=3
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=' ')
    print()
# A
# B B
# C C C
num=3
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()
# 1 2 3
# 1 2 3
# 1 2 3
n=3
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()
# 1
# 0 1
# 0 1 0
n = 3
for i in range(1, n + 1):
    for j in range(i):
        if i==1:
            print(1,end=" ")
        else:
            print(j % 2, end=" ")
    print()
#    *
#   **
#  ***
# ****
# n=4
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     print()
n=4
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(n-i+1):
        print("*",end="")
    print()
# ****
#  ***
#   **
#    *
n=4
for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(n-i+1):
        print(("*"),end="")
    print()
n=4
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()


