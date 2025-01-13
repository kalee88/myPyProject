class Pokemon:
    def __init__(self, name, health, typing, attack, currentHealth):
        self.name = name
        self.health = health
        self.typing = typing
        self.attack = attack
        self.currentHealth = currentHealth
    
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
        
        
def pokemonInformation(pokemon):
    return f"{pokemon.name} has {pokemon.health} health and {pokemon.attack} attack power"

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
