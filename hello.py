class Instagram:
    posts={}
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        self.__email=None
        self.__password=None
        self.friends=[]
        self.following=0
        self.followers=0
        self.logged=False
    @classmethod
    def signup(cls,name, email):
        pass
    def login(self,name,password):
        if self.name==name and self.__password==password:
            print("User is logged in successfully")
            self.logged=True
    def logout(self,name,password):
        if self.logged==True:
            self.logged=False
            print("User logged out successfully")
    def post(self):
        if self.logged==True:
            caption = input("Enter post caption")
            Instagram.posts[self.__email].append(caption)
            print("Post uploaded successfully")
        else:
            print("You need to login")
    def follow(self,other):
        if other not in self.friends:
            self.friends.append(other.name)
            self.following+=1
            other.followers+=1
            print(f"{self} is following {other.name} successfully")
        else:
            print(f"{self} is already following other")
    def unfollow(self,other):
        if other in self.friends:
            self.friends.remove(other)
            self.following-=1
            other.followers-=1
            print(f"{self} is not following {other.name} successfully")
        else:
            print(f"{self} is not a follower of {other.name}")
    def __str__(self):
        return (f"Name: {self.name}\nAge: {self.age}\nGender:{self.gender}\nFriends: {self.friends}\nFollowing: {self.following}\nFollowers: {self.followers}\n")

    def profile(self):
        print(self)
obj1=Instagram("Harshita",21,"Female")
obj2=Instagram("Vaishnavi",25,"Female")
obj1.profile()
obj1.follow(obj2)





