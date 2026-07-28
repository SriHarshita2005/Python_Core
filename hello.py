# class Instagram:
#     posts={}
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.__email=None
#         self.__password=None
#         self.friends=[]
#         self.following=0
#         self.followers=0
#         self.logged=False
#     @classmethod
#     def signup(cls,name, email):
#         pass
#     def login(self,name,password):
#         if self.name==name and self.__password==password:
#             print("User is logged in successfully")
#             self.logged=True
#     def logout(self,name,password):
#         if self.logged==True:
#             self.logged=False
#             print("User logged out successfully")
#     def post(self):
#         if self.logged==True:
#             caption = input("Enter post caption")
#             Instagram.posts[self.__email].append(caption)
#             print("Post uploaded successfully")
#         else:
#             print("You need to login")
#     def follow(self,other):
#         if other not in self.friends:
#             self.friends.append(other.name)
#             self.following+=1
#             other.followers+=1
#             print(f"{self} is following {other.name} successfully")
#         else:
#             print(f"{self} is already following other")
#     def unfollow(self,other):
#         if other in self.friends:
#             self.friends.remove(other)
#             self.following-=1
#             other.followers-=1
#             print(f"{self} is not following {other.name} successfully")
#         else:
#             print(f"{self} is not a follower of {other.name}")
#     def __str__(self):
#         return (f"Name: {self.name}\nAge: {self.age}\nGender:{self.gender}\nFriends: {self.friends}\nFollowing: {self.following}\nFollowers: {self.followers}\n")
#
#     def profile(self):
#         print(self)
# obj1=Instagram("Harshita",21,"Female")
# obj2=Instagram("Vaishnavi",25,"Female")
# obj1.profile()
# obj1.follow(obj2)

# a = [34 , 16 , 7 , 72 , 6 , 23]
# s = 0
# res = []
# for i in a:
#     if i%9 == 0:
#         r = i//9
#         res.append(r)
#         s += r
#     else:
#         r = (i // 9) + 1
#         res.append(r)
#         s += r
# print(res)
# print(s)

# def nearest_fibonacci():
#     while(True):

def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def is_fibonacci(n):
    a = 0
    b = 0
    while True:
        if a == n:
            return True

        c = a+b
        a = b
        b = c
a = list(map(int,input().split()))

# a = [2,2,3,4,2,3,5,7,2,7,6,3,4]
# for i in range(len(a)):
#     f = 0
#     for j in range(i, 0 , -1):
#         if a[i] == a[j]:
#             f+=1
#         if f == 2:
#             print(a[i],a[j])
#             break
a = [2,2,3,4,2,3,5,7,2,7,6,3,4]
seen = []
for x in a:
    if x in seen:
        print(x, x)
        seen.remove(x)   # pair completed
    else:
        seen.append(x)






