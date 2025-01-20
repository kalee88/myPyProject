class Pokemon:
    def __init__(self, name, health, typing, attack, currentHealth,speed):
        self.name = name
        self.health = health
        self.typing = typing
        self.attack = attack
        self.currentHealth = currentHealth
        self.speed = speed
    
    def setHealth(self, health):
        self.health = health
    
    def getHealth(self):
        return self.health
    
    def getName(self):
        return self.name
    
    def perform_attack(self, other_pokemon):
        # Ensure `other_pokemon` is an instance of the Pokemon class
        if isinstance(other_pokemon, Pokemon):
            other_pokemon.health -= 2
            self.health += 1
    
    def perform_attack2(self, other_pokemon):
        # Ensure `other_pokemon` is an instance of the Pokemon class
        if isinstance(other_pokemon, Pokemon):
            other_pokemon.health -= 2
            self.attack += 1
            
        
    def perform_potion(self):
        self.health = self.health + 2
        
    def perform_attackboost(self):
        self.attack = self.attack + 2
        
def askMove():
    user_input = input("Press 1 to do attack number 1, Press 2 to do attack number 2, Press 3 to potion, Press 4 to give attack boost")
    return user_input
    
def pokemonInformation(pokemon):
    return f"{pokemon.name} has {pokemon.health} health and {pokemon.attack} attack power"

while True:
    Latios = Pokemon("Latios", 8, "Dragon", 5, 8, 4)
    Latias = Pokemon("Latias", 7, "Dragon", 6, 7, 5)
    if (Latios.speed > Latias.speed):
        x = askMove()
        if (x == 1):
            Latios.perform_attack(Latias)
        if (x == 2):
            Latios.perform_attack2(Latias)
        if (x == 3):
            Latios.perform_potion()
        if (x == 4):
            Latios.perform_attackboost()
        y = askMove()
        if (y == 1):
            Latias.perform_attack(Latios)
        if (y == 2):
            Latias.perform_attack2(Latios)
        if (y == 3):
            Latias.perform_potion()
        if (y == 4):
            Latias.perform_attackboost()
    else:
        y = askMove()
        if (y == 1):
            Latias.perform_attack(Latios)
        if (y == 2):
            Latias.perform_attack2(Latios)
        if (y == 3):
            Latias.perform_potion()
        if (y == 4):
            Latias.perform_attackboost()
        x = askMove()
        if (x == 1):
            Latios.perform_attack(Latias)
        if (x == 2):
            Latios.perform_attack2(Latias)
        if (x == 3):
            Latios.perform_potion()
        if (x == 4):
            Latios.perform_attackboost()
    print(pokemonInformation(Latios))
    print(pokemonInformation(Latias))
    
'''
# Create two Pokemon instances
Garchomp = Pokemon("Garchomp", 5, "Dragon", 3, 5)
Dragonite = Pokemon("Dragonite", 8, "Dragon", 3, 8)

# Dragonite attacks Garchomp
Dragonite.perform_attack(Garchomp)

# Print information about both Pokemon
print(pokemonInformation(Garchomp))  # Garchomp's health
print(pokemonInformation(Dragonite))  # Dragonite's health
Garchomp.perform_potion()
print(pokemonInformation(Garchomp))  # Garchomp's health
Dragonite.perform_attackboost()
print(pokemonInformation(Dragonite))  # Garchomp's health
'''
