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








