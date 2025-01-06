class Pokemon:
    def __init__(self, name, health , typing, attack, currentHealth):
        self.name = name
        self.health = health
        self.typing = typing
        self.attack = attack
        self.currentHealth = currentHealth
    
    def setHealth(self,health):
        self.health = health
    
    def getHealth(self):
        return self.health
    
    def getName(self):
        return self.name
def pokemonInformation(Pokemon):
    return "Pokemon Name : " + Pokemon.name + " Pokemon Health: " + str(Pokemon.health)


Garchomp = Pokemon("Garchomp", 5, "Dragon", 3, 5)
print(pokemonInformation(Garchomp))
