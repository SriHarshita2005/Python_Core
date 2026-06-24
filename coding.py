# factors of a given number
import random

# n=int(input())
# for i in range(1,n+1):
#     if(n%i==0):
#         print(i,end=" ")

#count fo factors of a given number

# n=int(input())
# c=0
# for i in range(1,n+1):
#     if(n%i==0):
#         c+=1
# print(c)

#given number is prime or not

# n=int(input())
# fc=0
# for i in range(1,n+1):
#     if(n%i==0):
#         fc+=1
# if(fc==2):
#     print("Prime number")
# else:
#     print("Not a Prime Number")

#prime numbers upto n
# n=int(input())
# for i in range(1,n+1):
#     fc=0
#     for j in range(1,i+1):
#         if(i%j==0):
#             fc+=1
#     if(fc==2):
#         print(i,end=" ")

#prime numbers upto n using functions
# def is_prime(n):
#     fc=0
#     for i in range(1,n+1):
#         if(n%i==0):
#             fc+=1
#     if(fc==2):
#         return True
#     else:
#         return False
# a=1
# b=20
# for i in range(a,b+1):
#     if(is_prime(i)):
#         print(i,end=" ")

#print the following pattern 2+3+5+7+11+13+17+19=avg

# a=int(input())
# b=int(input())
# s=0
# c=0
# for i in range(a,b+1):
#     fc=0
#     for j in range(1,i+1):
#         if(i%j==0):
#             fc+=1
#     if(fc==2):
#         s=s+i
#         c=c+1
#         if(c>1):
#             print("+",end=" ")
#         print(i,end=" ")
# print(f"={s/c:.2f}.")

#print alternate prime numbers

# a=int(input())
# b=int(input())
# s=0
# c=0
# d=0
# for i in range(a,b+1):
#     fc=0
#     for j in range(1,i+1):
#         if(i%j==0):
#             fc+=1
#     if(fc==2):
#         d+=1
#         if(d%2==1):
#             s=s+i
#             c=c+1
#             if(c>1):
#                 print("+",end=" ")
#             print(i,end=" ")
# print(f"={s/c:.2f}.")

#N prime numbers eg input is 5 output is 2,3,5,7,11

# a=int(input())
# b=int(input())
# c=0
# while(True):
#     fc=0
#     for j in range(1,a+1):
#         if(a%j==0):
#             fc+=1
#     if(fc==2):
#             print(a,end=" ")
#             c+=1
#             if(c==b):
#                 break
#     a+=1

#in given digits finding prime numbers
# n=int(input())
# while(n!=0):
#     rem=n%10
#     fc=0
#     for i in range(1,rem+1):
#         if(rem%i==0):
#             fc+=1
#     if(fc==2):
#         print(rem,end=" ")
#     n=n//10

# n=int(input())
# while(n!=0):
#     rem=n%10
#     if(rem==2 or rem==3 or rem==5 or rem==7):
#         print(rem,end=" ")
#     n=n//10


#alt digits of a number
# n=int(input())
# c=0
# while(n!=0):
#     r=n%10
#     c+=1
#     if(c%2==1):
#         print(r,end="")
#     n=n//10


# a=int(input("Enter input"))
# power=len(str(a))
# temp=a
# s=0
# while(a!=0):
#     rem=a%10
#     s=s+(rem**power)
#     a=a//10
# if temp==s:
#     print("Armstrong number")9

# else:
#     print("Not an armstrong number")


# print("Number Guessing Game ")
# print("I'am thinking of a number from 1 to 100")
# secret_number=random.randint(1,100)
# attempts=0
# max_attempts=10
# while(attempts<=max_attempts):
#     attempts+=1
#     remaining=max_attempts-attempts +1
#     print(f"Attempts {attempts}/{max_attempts}")
#     try:
#         guess=int(input("Your guess:"))
#     except ValueError:
#         print("Please Enter Your Number")
#         continue
#     if guess==secret_number:
#         print("Winner")
#         break
#     elif guess<secret_number:
#         print("Too Low")
#     else:
#         print("Too High")
#     if remaining>1:
#         print(f"You have {remaining-1} attempts left")
#     else:
#         print(f"Game over! The secret number is {secret_number}")
# print("Thankyou for playing")



#circular prime
def is_prime(n):
    x=int(n**0.5)
    for i in range(2,x+1):
        if n %i == 0:
            return False
    return True
def is_circular(n):
    c=len(str(n))
    num=n
    e=c
    while e!=0:
        ld=num%10
        rem=num//10
        num=(ld*(10**(c-1)))+rem

        if is_prime(num):
            print(num)
        e-=1
# n=int(input())
# is_circular(n)

#first n prime numbers
# n=int(input())
# c=0
# p=2
# while True:
#     fc=0
#     for j in range(1,p+1):
#         if p%j==0:
#             fc+=1
#     if fc==2:
#         print(p,end=" ")
#         c+=1
#         if c==n:
#             break
#     p+=1

#Automorphic number
# n=int(input())
# square = n * n
# power = len(str(n))
# if square % 10**power == n:
#     print("Automorphic number")
# else:
#     print("Non automorphic number")

# neon number
# n=int(input())
# square = n * n
# temp = square
# s = 0
# while square > 0:
#     ld = square % 10
#     s += ld
#     square = square // 10
# if s == n:
#     print("Neon ")
# else:
#     print("Not neon")

#Duck number
# n=input()
# if '0' in n and n[0] !=0:
#     print("Duck number")
# else:
#     print("Not a duck number")

# spy number
# n=int(input())
# s=0
# p=1
# temp = n
# while n>0:
#     ld = n%10
#     s=s+ld
#     p=p*ld
#     n=n//10
# if s==p:
#     print("spy number")
# else:
#     print("Not a spy number")

#Happy number
# n=int(input())
# while n!=1 and n!=4:
#     s=0
#     while n>0:
#         ld =n%10
#         s=s+ld*ld
#         n=n//10
#     n=s
# if n==1:
#     print("Happy number")
# else:
#     print("Not happy number")

#Strong number
# n=int(input())
# temp = n
# s=0
# while n>0:
#     fact = 1
#     ld = n%10
#     for i in range(1,ld+1):
#         fact=fact*i
#     s=s+fact
#     n=n//10
# if s ==temp:
#     print("Strong number")
# else:
#     print("Not a strong number")

#Emrip numbers
# def is_prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# n=int(input())
# temp = n
# rev = 0
# while n>0:
#     rem = n%10
#     rev = rev*10+rem
#     n=n//10
# if is_prime(rev) and is_prime(temp) and temp !=rev:
#     print("Emrip number")
# else:
#     print("Not a emrip number")

#disarium number
# n=int(input())
# temp = n
# digits = 0
# t=n
# while t >0:
#     digits += 1
#     t=t//10
# s=0
# t=n
# while t>0:
#     ld = n%10
#     s=s+ld**digits
#     digits-=1
#     n=n//10
# if s==temp:
#     print("Disarium number")
# else:
#     print("Not a disarium number")

Armstrong
Strong
Neon
Duck
Spy
Automorphic
Happy
Emirp
Disarium
Fascinating
Keith
Smith
Circular Prime
Adam
Tech
Kaprekar
Harshad
Buzz
Sunny
Perfect Number




