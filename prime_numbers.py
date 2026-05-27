#first n prime numbers
def first_n_primes(n):
    c=0
    p=2
    while True:
        fc=0
        for j in range(1,p+1):
            if p%j==0:
                fc+=1
        if fc==2:
            print(p,end=" ")
            c+=1
            if c==n:
                break
        p+=1
# n=int(input())
# first_n_primes(n)

#prime numbers upto n
def prime_upto_n(n):
    for i in range(1,n+1):
        fc=0
        for j in range (1,i+1):
            if i%j==0:
                fc+=1
        if fc==2:
            print(i,end=" ")
# n=int(input())
# prime_upto_n(n)


#check whether a number is prime or not
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        else :
            return True
# n=int(input())
# print(is_prime(n))

#Count total prime numbers between 1 and N.
def count(n):
    c=0
    for i in range(1,n+1):
        fc=0
        for j in range(1,i+1):
            if i%j==0:
                fc+=1
        if fc==2:
            c+=1
    print(c)
# n=int(input())
# count(n)

#Find the sum of all prime numbers up to N.
def sum_of_n(n):
    s=0
    for i in range(1,n+1):
        fc=0
        for j in range(1,i+1):
            if i%j==0:
                fc+=1
        if fc==2:
            s+=i
    print(s)
# n=int(input())
# sum_of_n(n)

#Find the average of prime numbers in a range.
def avg_of_n(n):
    s=0
    c=0
    for i in range(1,n+1):
        fc=0
        for j in range(1,i+1):
            if i%j==0:
                fc+=1
        if fc==2:
            s+=i
            c+=1
    print(s/c)
# n=int(input())
# avg_of_n(n)

#Print prime numbers between two given numbers.
def prime_between_aandb(a,b):
    for i in range(a,b+1):
        fc=0
        for j in range(1,i+1):
            if i%j==0:
                fc+=1
        if fc==2:
            print(i,end=" ")
# a=int(input())
# b=int(input())
# prime_between_aandb(a,b)


#Find the smallest prime number greater than N.
def sp(n):
    a=n
    while True:
        fc=0
        for i in range(1,a+1):
            if a%i==0:
                fc+=1
        if fc==2:
            print(a)
            break
        a+=1
# n=int(input())
# sp(n)


#Find the largest prime number less than N.
def lp(n):
    for i in range(n,1,-1):
        fc=0
        for j in range(1,i+1):
            if i%j==0:
                fc+=1
        if fc==2:
            print(i)
            break
# n=int(input())
# lp(n)


#Check whether a number is composite or prime.
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return "Composite number"
        else:
            return "Prime number"
# n=int(input())
# print(is_prime(n))

#Find the nth prime number.
def nth_pn(n):
    p=2
    c=0
    while True:
        fc=0
        for i in range(1,p+1):
            if p%i==0:
                fc+=1
        if fc==2:
            c+=1
            if c==n:
                print(p)
                break
        p+=1
# n=int(input())
# nth_pn(n)


#Print prime numbers in reverse order.
def reverse_order(n):
    for i in range(n,1,-1):
        fc=0
        for j in range(1,i+1):
            if i%j==0:
                fc+=1
        if fc==2:
            print(i,end=" ")
# n=int(input())
# reverse_order(n)


#Count how many prime digits are present in a number.
def prime_digits(n):
    while(n!=0):
        rem=n%10
        fc=0
        for i in range(1,rem+1):
            if rem%i==0:
                fc+=1
        if fc==2:
            print(rem,end=" ")
        n=n//10
# n=int(input())
# prime_digits(n)


#Find the product of prime numbers in a range.