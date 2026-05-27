#Create a Character class with: • private _health • methods to damage(points) and heal(points)
# • health cannot drop below 0 or exceed max limit • expose only current health through a read-only getter

class Character:
    def __init__(self,health):
        self.__health=health
