#Create a Character class with: • private _health • methods to damage(points) and heal(points)
# • health cannot drop below 0 or exceed max limit • expose only current health through a read-only getter

class Character:
    def __init__(self,health):
        self.max_limit=100
        if (health>=0) and (health) <= self.max_limit:
            self.__health=health
        else:
            self.__health=0
    def damage(self,points):
        self.__health-=points
        if self.__health<0:
            self.__health=0
            return self.__health
        else:
            return self.__health
    def heal(self,points):
        self.__health+=points
        if self.__health>self.max_limit:
            self.__health=self.max_limit
        else:
            return self.__health
    @property
    def display(self):
        return self.__health
c1=Character(50)
c1.damage(20)
print(c1.display)
c1.heal(90)
print(c1.display)
