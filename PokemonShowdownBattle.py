import Random
isFlinch = False
class Pokemon:
    def __init__(self, name, health, typing, attack, speed, defense, ability):
        self.name = name
        self.health = health
        self.typing = typing
        self.attack = attack
        self.speed = speed
        self.defense = defense
        self.ability = ability
    
    def setHealth(self, health):
        self.health = health
    
    def getHealth(self):
        return self.health
    
    def getName(self):
        return self.name
    
    def perform_potion(self):
        self.health = self.health + 20

    def getAttack(self):
        return self.attack

    def getDefense(self):
        return self.defense

    def getTyping(self):
        return self.typing

    def getSpeed(self):
        return self.speed

    def setSpeed(self, speed):
        self.speed = speed

    def setAttack(self, attack):
        self.attack = attack

    def getAbility(self):
        return self.ability
        
class Flygon(Pokemon):
    def __init__(self, name, health, typing, attack, speed, ability):
        super().__init__(
            name = "Flygon",
            health = 80,
            typing = "Dragon",
            attack = 100,
            speed = 100,
            defense = 80,
            ability = "Levitate"
        )
    def Dragon_Claw(self,target):
        damage = (80 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Dragon":
            damage = damage*2
        if target.getTyping() == "Steel":
            damage = damage*.5
        if target.getTyping() == "Fairy":
            damage = 0
        damage = damage * 1.25
        target.setHealth(target.getHealth() - damage)

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
        target.setHealth(target.getHealth() - damage)

    def Dragon_Dance(self):
        if (speed < 6):
            self.setSpeed(self.getSpeed() + 1)
        if (attack < 6):
            self.setAttack(self.getAttack() + 1)

    def Giga_Drain(self,target):
        damage = (75 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Water" or target.getTyping() == "Ground" or target.getTyping() == "Rock":
            damage = damage*2
        if target.getTyping() == "Fire" or target.getTyping() == "Grass" or target.getTyping() == "Poison" or target.getTyping() == "Flying" or target.getTyping() == "Bug" or target.getTyping() == "Dragon" or target.getTyping() == "Steel":
            damage = damage*.5
        target.setHealth(target.getHealth() - damage)
        self.setHealth(target.getHealth() + damage*0.5)
flygon = Flygon()        


class Baxcalibur(Pokemon):
    def __init__(self, name, health, typing, attack, speed, ability):
        super().__init__(
            name = "Baxcalibur",
            health = 115,
            typing = "Dragon",
            attack = 145,
            speed = 87,
            defense = 90,
            ability = "Thermal Exchange/Ice Body"
        )
        def Glaive_Rush(self,target):
        damage = (120 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Dragon":
            damage = damage*2
        if target.getTyping() == "Steel":
            damage = damage*.5
        if target.getTyping() == "Fairy":
            damage = 0
        damage = damage * 1.25
        self.setHealth(self.getHealth() - damage*(.15))
        target.setHealth(target.getHealth() - damage)

    def Icicle_Crash(self,target):
        global isFlinch
        damage = (85 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Grass" or target.getTyping() == "Ground" or target.getTyping() == "Flying" or target.getTyping() == "Dragon":
            damage = damage*2
        if target.getTyping() == "Steel" or target.getTyping() == "Fire" or target.getTyping() == "Water" or target.getTyping() == "Ice":
            damage = damage*.5
        accuracy = random.randint(1,100)
        if (accuracy > 90 and accuracy < 101):
            damage = 0
        flinchChance = random.randint(1,100)
        if (flinchChance > 70 and flinchChance < 101):
            isFlinch = True
        target.setHealth(target.getHealth() - damage)

    def Dragon_Dance(self):
        if (speed < 6):
            self.setSpeed(self.getSpeed() + 1)
        if (attack < 6):
            self.setAttack(self.getAttack() + 1)

    def Recover(self):
        self.setHealth(self.getHealth() + self.getHealth()*0.5)


def askMove(pokemon):
    user_input = input(f"It is {pokemon.name}'s turn! Press 1 to do attack number 1, Press 2 to do attack number 2, Press 3 to potion, Press 4 to give attack boost: ")
    
    # Convert the input to an integer
    return int(user_input)
    
def pokemonInformation(pokemon):
    return f"{pokemon.name} has {pokemon.health} health and {pokemon.attack} attack power"
#Remember to add isFlinch global variable in our simulation loop.

def battle():
    global isFlinch
    while self.getHealth() > 0 and opponent.getHealth() > 0:

battle()
























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
