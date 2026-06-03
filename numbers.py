#Count number of digits in a number.

def count(n):
    c=0
    while(n!=0):
        c+=1
        n=n//10
    print(c)
# n=int(input())
# count(n)
# Find sum of digits.

def sum1(n):
    s=0
    while(n!=0):
        rem=n%10
        s=s+rem
        n=n//10
    print(s)
# n=int(input())
# sum1(n)

# Find product of digits.

def product(n):
    p=1
    while(n!=0):
        rem=n%10
        p=p*rem
        n=n//10
    print(p)
# n=int(input())
# product(n)

# Reverse a number.

def reverse(n):
    rev=0
    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    print(rev)
# n=int(input())
# reverse(n)

# Check palindrome number.

def palindrome(n):
    rev=0
    temp=n
    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if temp==rev:
        print("Palindrome")
    else:
        print("Not a palindrome")
# n=int(input())
# palindrome(n)

# Find largest digit.

def largest(n):
    h=0
    while(n!=0):
        rem=n%10
        if rem>h:
            h=rem
        n=n//10
    print(h)
# n=int(input())
# largest(n)

# Find smallest digit.

def smallest(n):
    s=9
    while(n!=0):
        rem=n%10
        if rem<s:
            s=rem
        n=n//10
    print(s)
# n=int(input())
# smallest(n)

# Print digits individually.

def digits(n):
    rev=0
    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    while(rev!=0):
        ld=rev%10
        print(ld,end=" ")
        rev=rev//10
# n=int(input())
# digits(n)

# Count even digits and odd digits.

def eocount(n):
    ec=0
    oc=0
    while(n!=0):
        rem=n%10
        if rem%2==0:
            ec+=1
        else:
            oc+=1
        n=n//10
    print(oc,ec)
# n=int(input())
# eocount(n)

# Find sum of even digits.

def sume(n):
    s=0
    while(n!=0):
        rem=n%10
        if rem%2==0:
            s+=rem
        n=n//10
    print(s)
# n=int(input())
# sume(n)

# Find sum of odd digits.

def sumo(n):
    s=0
    while(n!=0):
        rem=n%10
        if rem%2==1:
            s+=rem
        n=n//10
    print(s)
# n=int(input())
# sumo(n)

# Find average of digits.

def average(n):
    s=0
    c=0
    while(n!=0):
        rem=n%10
        c+=1
        s+=rem
        n=n//10
    print(s/c)
# n=int(input())
# average(n)

# Find first digit of a number.

def fd(n):
    while(n>=10):
        n=n//10
    print(n)
# n=int(input())
# fd(n)

# Remove last digit from a number.

def ld(n):
    n=n//10
    print(n)
# n=int(input())
# ld(n)

# Check whether a number contains 0.

def check(n):
    while(n!=0):
        rem=n%10
        if rem==0:
            print("0 found")
            break
        n=n//10
# n=int(input())
# check(n)

# Count occurrences of a digit.

def occurances(n):
    digit=3
    count=0
    while(n!=0):
        rem=n%10
        if digit==rem:
            count+=1
        n=n//10
    print(count)
# n=int(input())
# occurances(n)

# Find difference between sum of even and odd digits.

def diff(n):
    es=0
    os=0
    while(n!=0):
        rem=n%10
        if rem%2==0:
            es+=rem
        else:
            os+=rem
        n=n//10
    print(os-es)
# n=int(input())
# diff(n)

# Check whether all digits are same.

def same(n):
    while(n!=0):
        rem=n%10
        if n==rem:
            print("Same")
        n=n//10
# n=int(input())
# same(n)

# Find second largest digit.

def second_largest(n):
    l=0
    sl=0
    while(n!=0):
        rem=n%10
        if rem>l:
            sl=l
            l=rem
        elif rem>sl and rem!=l:
            sl=rem
        n=n//10
    print(sl)
# n=int(input())
# second_largest(n)
