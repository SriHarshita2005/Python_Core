# ARRAY/LIST PRACTICE SHEET
# Part 1: Basics
# 1. Find the Largest Element
# Input
# 10 4 25 8 15
# Output
# 25

# a = list(map(int,input().split()))
# maxi = a[0]
# for i in a:
#     if i > maxi:
#         maxi = i
# print(maxi)

# 2. Find the Smallest Element
# Input
# 10 4 25 8 15
# Output
# 4

# a = list(map(int,input().split()))
# mini = a[0]
# for i in a:
#     if i < mini:
#         mini = i
# print(mini)

# 3. Find the Second Largest Element
# Input
# 10 4 25 8 15
# Output
# 15

a = list(map(int,input().split()))
first = 0
second = 0
for i in range(len(a)):
    if a[i] > first:
        second = first
        first = a[i]
    elif a[i] > second and a[i] != first:
        second = a[i]
print(second)

# 4. Find the Second Smallest Element
# Input
# 10 4 25 8 15
# Output
# 8

a = list(map(int,input().split()))
first = float('inf')
second = float('inf')
for i in range(len(a)):
    if a[i] < first:
        second = first
        first = a[i]
    elif a[i] < second and a[i] != first:
        second = a[i]
print(second)

# 5. Sum of Elements
# Input
# 2 5 8 10
# Output
# 25

a = list(map(int,input().split()))
s = 0
for i in a:
    s = s+i
print(s)

# 6. Average of Elements
# Input
# 2 5 8 10
# Output
# 6.25

# a = list(map(int,input().split()))
# s = 0
# c = 0
# for i in a:
#     s = s + i
#     c = c + 1
# print(s/c)

# 7. Count Even and Odd Numbers
# Input
# 1 2 3 4 5 6
# Output
# Even = 3
# Odd = 3

a = list(map(int,input().split()))
e,o = 0,0
for i in a:
    if i%2 == 0:
        e+=1
    else:
        o+=1
print(e,o)

# 9. Reverse a List
# Input
# 1 2 3 4 5
# Output
# 5 4 3 2 1

a = list(map(int,input().split()))
for i in range(len(a)-1 , -1, -1):
    print(a[i],end = " ")

# 10. Linear Search
# Find whether 25 exists.
# Input
# 10 20 25 30 40
# Output
# Found

a = list(map(int,input().split()))
key = int(input())
for i in a:
    if key == i:
        print("Found")
        break
else:
    print("Not found")

# 11. Count Occurrences
# Find occurrences of 3.
# Input
# 1 3 2 3 4 3 5
# Output
# 3

a = list(map(int,input().split()))
k = int(input())
c = 0
for i in a:
    if i == k:
        c+=1
print(c)

# 12. Print Frequency of Every Element
# Input
# 2 3 2 5 3 2
# Output
# 2 -> 3
# 3 -> 2
# 5 -> 1

a = list(map(int,input().split()))

for i in range(len(a)):
    c = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            c+=1
    print(c,end = " ")

# 13. Most Frequent Element
# Input
# 2 3 2 5 3 2
# Output
# 2

a = list(map(int,input().split()))
maxi = 0
element = a[0]
for i in range(len(a)):
    c = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            c+=1
    if c > maxi:
        maxi = c
        element = a[i]
print(element)

# 14. Least Frequent Element
# Input
# 2 3 2 5 3 2
# Output
# 5

a = list(map(int,input().split()))
mini = float('inf')
element = a[0]
for i in range(len(a)):
    c = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            c+=1
    if c < mini:
        mini = c
        element = a[i]
print(element)

# 15. Remove Duplicates
# Input
# 1 2 2 3 4 3 5
# Output
# 1 2 3 4 5

