import Random
class Pokemon:
    def __init__(self, name, health, typing, attack, currentHealth, speed, defense):
        self.name = name
        self.health = health
        self.typing = typing
        self.attack = attack
        self.currentHealth = currentHealth
        self.speed = speed
        self.defense = defense
    
    def setHealth(self, health):
        self.health = health
    
    def getHealth(self):
        return self.health
    
    def getName(self):
        return self.name
    
    def perform_potion(self):
        self.currentHealth = self.currentHealth + 20

    def getAttack(self):
        return self.attack

    def getDefense(self):
        return self.defense

    def getTyping(self):
        return self.typing

class Flygon(Pokemon):
    def __init__(self, name, health, typing, attack, currentHealth, speed):
        super().__init__(
            name = "Flygon",
            health = 80,
            typing = "Dragon",
            attack = 100,
            currentHealth = 100
            speed = 100
            defense = 80
        )
        )
    def Dragon_Claw(self,target):
        damage = (80 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Dragon":
            damage = damage*2
        if target.getTyping() == "Steel":
            damage = damage*.5
        if target.getTyping() == "Fairy":
            damage = 0
        return damage

    def Fire_Blast(self,target):
        damage = (110 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Grass" or target.getTyping() == "Ice" or target.getTyping() == "Bug" or target.getTyping() == "Steel":
            damage = damage*2
        if target.getTyping() == "Steel":
            damage = damage*.5
        if target.getTyping() == "Fairy":
            damage = 0
        accuracy = random.randint(1,100)
        if (accuracy > 85 and accuracy < 101):
            damage = 0
        return damage
    
flygon = Flygon()        
        
def askMove(pokemon):
    user_input = input(f"It is {pokemon.name}'s turn! Press 1 to do attack number 1, Press 2 to do attack number 2, Press 3 to potion, Press 4 to give attack boost: ")
    
    # Convert the input to an integer
    return int(user_input)
    
def pokemonInformation(pokemon):
    return f"{pokemon.name} has {pokemon.health} health and {pokemon.attack} attack power"

while True:

























    '''
    if Latios.speed > Latias.speed:
        x = askMove(Latios)
        if x == 1:
            Latios.perform_attack(Latias)
            print(pokemonInformation(Latias))
        if x == 2:
            Latios.perform_attack2(Latias)
            print(pokemonInformation(Latias))
        if x == 3:
            Latios.perform_potion()
            print(pokemonInformation(Latios))
        if x == 4:
            Latios.perform_attackboost()
            print(pokemonInformation(Latios))
        
        y = askMove(Latias)
        if y == 1:
            Latias.perform_attack(Latios)
            print(pokemonInformation(Latios))
        if y == 2:
            Latias.perform_attack2(Latios)
            print(pokemonInformation(Latios))
        if y == 3:
            Latias.perform_potion()
            print(pokemonInformation(Latias))
        if y == 4:
            Latias.perform_attackboost()
            print(pokemonInformation(Latias))
    else:
        y = askMove(Latias)
        if y == 1:
            Latias.perform_attack(Latios)
            print(pokemonInformation(Latios))
        if y == 2:
            Latias.perform_attack2(Latios)
            print(pokemonInformation(Latios))
        if y == 3:
            Latias.perform_potion()
            print(pokemonInformation(Latias))
        if y == 4:
            Latias.perform_attackboost()
            print(pokemonInformation(Latias))
        
        x = askMove(Latios)
        if x == 1:
            Latios.perform_attack(Latias)
            print(pokemonInformation(Latias))
        if x == 2:
            Latios.perform_attack2(Latias)
            print(pokemonInformation(Latias))
        if x == 3:
            Latios.perform_potion()
            print(pokemonInformation(Latios))
        if x == 4:
            Latios.perform_attackboost()
            print(pokemonInformation(Latios))
'''
