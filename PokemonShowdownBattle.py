import Random
isFlinch = False
class Pokemon:
    def __init__(self, name, health, typing, attack, speed, defense, ability,moves,status, maxHealth):
        self.name = name
        self.health = health
        self.typing = typing
        self.attack = attack
        self.speed = speed
        self.defense = defense
        self.ability = ability
        self.moves = moves
        self.status = status
        self.maxHealth = maxHealth
    
    def setHealth(self, health):
        self.health = health
    
    def getHealth(self):
        return self.health

    def getmaxHealth(self):
        return self.maxHealth
        
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

    def setStatus(self, status):
        self.status = status
    def getStatus(self):
        return self.status

    def getAbility(self):
        return self.ability

    def getMoves(self):
        return self.moves
        
class Flygon(Pokemon):
    def __init__(self, name, health, typing, attack, speed, ability,status,maxHealth):
        super().__init__(
            name = "Flygon",
            health = 200,
            typing = "Dragon",
            attack = 100,
            speed = 100,
            defense = 80,
            ability = "Levitate"
            moves = ["Dragon_Claw", "Fire_Blast", "Dragon_Dance", "Giga_Drain"]
            status = []
            maxHealth = 200
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
    def askMove():
        while True:
            user_input = int(input("Type 1 to do Dragon Claw, Type 2 to do Fire Blast, Type 3 to do Dragon Dance, Type 4 to do Giga Drain!"))
            if user_input == 1:
                return Dragon_Claw
            if user_input == 2:
                return Fire_Blast
            if user_input == 3:
                return Dragon_Dance
            if user_input == 4:
                return Giga_Drain
            
flygon = Flygon()        

class eevee(Pokemon):
    def __init__(self, name, health, typing, attack, speed, ability, moves,status,maxHealth):
        eeveelutions = ["Vaporeon", "Glaceon", "Flareon", "Leafeon", "Jolteon", "Umbreon", "Sylveon", "Espeon"]
        eeveelutionType = ["Water", "Ice", "Fire", "Grass", "Electric", "Dark", "Fairy", "Psychic"]
        randomEevee = eeveelutions[random.randint(0,7)]
        randomEeveeType = eeveelutionType[random.randint(0,7)]
        super().__init__(
            name = randomEevee,
            health = 300,
            typing = randomEeveeType,
            attack = 110,
            speed = 110,
            defense = 100,
            ability = "N/A"
            moves = []
            status = []
            maxHealth = 300
        )
    def Hydro_Pump(self,target):
        damage = (110 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Fire" or target.getTyping() == "Rock" or target.getTyping() == "Ground" or target.getTyping() == "Steel":
            damage = damage*2
        if target.getTyping() == "Water" or target.getTyping() == "Grass" or target.getTyping() == "Dragon":
            damage = damage*.5
        accuracy = random.randint(1,100)
        if (accuracy > 80 and accuracy < 101):
            damage = 0
        target.setHealth(target.getHealth() - damage)

    def Water_Pulse(self,target):
        damage = (60 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Fire" or target.getTyping() == "Rock" or target.getTyping() == "Ground" or target.getTyping() == "Steel":
            damage = damage*2
        if target.getTyping() == "Water" or target.getTyping() == "Grass" or target.getTyping() == "Dragon":
            damage = damage*.5
        target.setHealth(target.getHealth() - damage)
        isFrozen = random.randint(1,5)
        if (isFrozen == 2):
            if not target.getAbility() == "Own Tempo":
                target.setStatus(target.getStatus += "Frozen")
                
    def Blizzard(self,target):
        damage = (110 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Grass" or target.getTyping() == "Dragon" or target.getTyping() == "Ground" or target.getTyping() == "Flying":
            damage = damage*2
        if target.getTyping() == "Water" or target.getTyping() == "Fire" or target.getTyping() == "Ice" or target.getTyping() == "Steel":
            damage = damage*.5
        accuracy = random.randint(1,100)
        if (accuracy > 70 and accuracy < 101):
            damage = 0
        target.setHealth(target.getHealth() - damage)
        isFrozen = random.randint(1,10)
        if (isFrozen == 7):
            if not target.getTyping() == "Ice" or not target.getAbility() == "Magma Armor":
                target.setStatus(target.getStatus += "Frozen")
                
    def Ice_Fang(self,target):
        damage = (65 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Grass" or target.getTyping() == "Dragon" or target.getTyping() == "Ground" or target.getTyping() == "Flying":
            damage = damage*2
        if target.getTyping() == "Water" or target.getTyping() == "Fire" or target.getTyping() == "Ice" or target.getTyping() == "Steel":
            damage = damage*.5
        accuracy = random.randint(1,100)
        if (accuracy > 95 and accuracy < 101):
            damage = 0
        target.setHealth(target.getHealth() - damage)
        isFrozen = random.randint(1,10)
        if (isFrozen == 7):
            if not target.getTyping() == "Ice" or not target.getAbility() == "Magma Armor":
                target.setStatus(target.getStatus += "Frozen")
        isFlinch = random.randint(1,10)
        if (isFlinch == 7):
            target.setStatus(target.getStatus += "Flinched")
            
    def Flare_Blitz(self,target):
        damage = (120 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Grass" or target.getTyping() == "Ice" or target.getTyping() == "Bug" or target.getTyping() == "Steel":
            damage = damage*2
        if target.getTyping() == "Water" or target.getTyping() == "Fire" or target.getTyping() == "Dragon" or target.getTyping() == "Rock":
            damage = damage*.5
        accuracy = random.randint(1,100)
        isCriticalHit = random.randint(1,24)
        if (isCrticalHit == 7):
            damage = 1.9 * damage
        target.setHealth(target.getHealth() - damage)
        self.setHealth(self.getHealth() - (damage * (1/3)))
        isBurn = random.randint(1,10)
        if (isBurn == 7):
            if not target.getTyping() == "Fire" or not target.getAbility() == "Water Veil":
                target.setStatus(target.getStatus += "Burn")
                
    def Fire_Fang(self,target):
        damage = (65 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Grass" or target.getTyping() == "Ice" or target.getTyping() == "Bug" or target.getTyping() == "Steel":
            damage = damage*2
        if target.getTyping() == "Water" or target.getTyping() == "Fire" or target.getTyping() == "Dragon" or target.getTyping() == "Rock":
            damage = damage*.5
        accuracy = random.randint(1,100)
        if (accuracy > 95 and accuracy < 101):
            damage = 0
        isCriticalHit = random.randint(1,24)
        if (isCrticalHit == 7):
            damage = 1.9 * damage
        target.setHealth(target.getHealth() - damage)
        isBurn = random.randint(1,10)
        if (isBurn == 7):
            if not target.getTyping() == "Fire" or not target.getAbility() == "Water Veil":
                target.setStatus(target.getStatus += "Burn")
        isFlinch = random.randint(1,10)
        if (isFlinch == 7):
            target.setStatus(target.getStatus += "Flinched")

    def Leaf_Blade(self,target):
        damage = (90 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Water" or target.getTyping() == "Ground" or target.getTyping() == "Rock":
            damage = damage*2
        if target.getTyping() == "Grass" or target.getTyping() == "Fire" or target.getTyping() == "Poison" or target.getTyping() == "Flying" or target.getTyping() == "Bug" or target.getTyping() == "Dragon" or target.getTyping() == "Steel":
            damage = damage*.5
        accuracy = random.randint(1,100)
        isCriticalHit = random.randint(1,8)
        if (isCrticalHit == 7):
            damage = 1.9 * damage
        target.setHealth(target.getHealth() - damage)
        
    def Magical_Leaf(self,target):
        damage = (60 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Water" or target.getTyping() == "Ground" or target.getTyping() == "Rock":
            damage = damage*2
        if target.getTyping() == "Grass" or target.getTyping() == "Fire" or target.getTyping() == "Poison" or target.getTyping() == "Flying" or target.getTyping() == "Bug" or target.getTyping() == "Dragon" or target.getTyping() == "Steel":
            damage = damage*.5
        accuracy = random.randint(1,100)
        isCriticalHit = random.randint(1,24)
        if (isCrticalHit == 7):
            damage = 1.9 * damage
        target.setHealth(target.getHealth() - damage)
        
        
    def Thunder(self,target):
        damage = (110 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Water" or target.getTyping() == "Flying" or target.getTyping() == "Rock":
            damage = damage*2
        if target.getTyping() == "Grass" or target.getTyping() == "Electric" or target.getTyping() == "Dragon":
            damage = damage*.5
        if target.getTyping() == "Ground":
            damage = 0
        accuracy = random.randint(1,100)
        if (accuracy > 70 and accuracy < 101):
            damage = 0
        isCriticalHit = random.randint(1,24)
        if (isCrticalHit == 7):
            damage = 1.9 * damage
        target.setHealth(target.getHealth() - damage)
    
    def Thunder_Fang(self,target):
        damage = (65 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Water" or target.getTyping() == "Flying" or target.getTyping() == "Rock":
            damage = damage*2
        if target.getTyping() == "Grass" or target.getTyping() == "Electric" or target.getTyping() == "Dragon":
            damage = damage*.5
        if target.getTyping() == "Ground":
            damage = 0
        accuracy = random.randint(1,100)
        if (accuracy > 95 and accuracy < 101):
            damage = 0
        isCriticalHit = random.randint(1,24)
        if (isCrticalHit == 7):
            damage = 1.9 * damage
        target.setHealth(target.getHealth() - damage)
        isPara = random.randint(1,10)
        if (isPara == 7):
            if not target.getTyping() == "Electric" or not target.getAbility() == "Limber":
                target.setStatus(target.getStatus += "Paralyzed")
        isFlinch = random.randint(1,10)
        if (isFlinch == 7):
            target.setStatus(target.getStatus += "Flinched")
    def Dark_Pulse(self,target):
        damage = (110 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Psychic" or target.getTyping() == "Ghost":
            damage = damage*2
        if target.getTyping() == "Fighting" or target.getTyping() == "Dark" or target.getTyping() == "Fairy":
            damage = damage*.5
        if target.getTyping() == "Ground":
            damage = 0
        isCriticalHit = random.randint(1,24)
        if (isCrticalHit == 7):
            damage = 1.9 * damage
        target.setHealth(target.getHealth() - damage)
        isFlinch = random.randint(1,20)
        if (isFlinch == 7 or isFlinch == 14):
            target.setStatus(target.getStatus += "Flinched")
            
    def Assurance(self,target):
        if (target.getHealth < target.maxHealth):
            damage = (120 * (self.getAttack() / target.getDefense())) / 50
        else:
            damage = (60 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Psychic" or target.getTyping() == "Ghost":
            damage = damage*2
        if target.getTyping() == "Fighting" or target.getTyping() == "Dark" or target.getTyping() == "Fairy":
            damage = damage*.5
        if target.getTyping() == "Ground":
            damage = 0
        isCriticalHit = random.randint(1,24)
        if (isCrticalHit == 7):
            damage = 1.9 * damage
        
        target.setHealth(target.getHealth() - damage)

    
    def Moonblast(self,target):
        damage = (95 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Dragon" or target.getTyping() == "Fighting" or target.getTyping() == "Dark":
            damage = damage*2
        if target.getTyping() == "Fire" or target.getTyping() == "Poison" or target.getTyping() == "Steel":
            damage = damage*.5
        if target.getTyping() == "Ground":
            damage = 0
        isCriticalHit = random.randint(1,24)
        if (isCrticalHit == 7):
            damage = 1.9 * damage
        target.setHealth(target.getHealth() - damage)
        
    def Draining_Kiss(self,target):
        damage = (50 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Dragon" or target.getTyping() == "Fighting" or target.getTyping() == "Dark":
            damage = damage*2
        if target.getTyping() == "Fire" or target.getTyping() == "Poison" or target.getTyping() == "Steel":
            damage = damage*.5
        if target.getTyping() == "Ground":
            damage = 0
        isCriticalHit = random.randint(1,24)
        if (isCrticalHit == 7):
            damage = 1.9 * damage
        target.setHealth(target.getHealth() - damage)
        healthGained = damage * .75
        self.setHealth(self.getHealth() + healthGained)
    def Psychic(self, target):
        damage = (90 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Fighting" or target.getTyping() == "Poison":
            damage = damage * 2
        if target.getTyping() == "Psychic" or target.getTyping() == "Steel":
            damage = damage * 0.5
        if target.getTyping() == "Dark":
            damage = 0
        accuracy = random.randint(1, 100)
        if accuracy > 90:
            damage = 0
        isCriticalHit = random.randint(1,24)
        if (isCrticalHit == 7):
            damage = 1.9 * damage
        target.setHealth(target.getHealth() - damage)
        isSpecialDefenseDrop = random.randint(1, 10)
        if isSpecialDefenseDrop == 7:
            target.setDefense(target.getDefense() - 1)

    def Psybeam(self,target):
        damage = (65 * (self.getAttack() / target.getDefense())) / 50
        if target.getTyping() == "Fighting" or target.getTyping() == "Poison":
            damage = damage * 2
        if target.getTyping() == "Psychic" or target.getTyping() == "Steel":
            damage = damage * 0.5
        if target.getTyping() == "Dark":
            damage = 0
        isConfused = random.randint(1,10)
        if (isConfused == 7):
            target.setStatus(target.getStatus += "Confused")
class Baxcalibur(Pokemon):
    def __init__(self, name, health, typing, attack, speed, ability, moves,status):
        super().__init__(
            name = "Baxcalibur",
            health = 230,
            typing = "Dragon",
            attack = 145,
            speed = 87,
            defense = 90,
            ability = "Thermal Exchange/Ice Body"
            moves = []
            status = []
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
'''
def battle():
    global isFlinch
    while self.getHealth() > 0 and opponent.getHealth() > 0:
        randomPokemon = random.randint(1,2)
        if randomPokemon == 1:
            player = Baxcalibur()
            opponent = Flygon()
            if player.getSpeed() > opponent.getSpeed():
                ourMove = player.askMove()
                if (ourMove == "Dragon_Dance" or "Recover") : 
                    player.ourMove()
                else : 
                    player.ourMove(opponent)
        else:
            opponent = Baxcalibur()
            player = Flygon()
            if player.getSpeed() > opponent.getSpeed():
                ourMove = player.askMove()
                if (ourMove == "Dragon_Dance") : 
                    player.ourMove()
                else : 
                    player.ourMove(opponent)
                opponentMoves = ["Glaive_Rush", "Icicle_Crash", "Dragon_Dance", "Recover"]
                opponentMove = random.randint(0,3)
                if opponentMove == 0:
                    opponentMoves[opponentMove]()
            else:
                opponentMoves
                
        

battle()
'''

def battle():
    global isFlinch

    # Create two Pokemon instances
    player = eevee("Eevee", 300, "Normal", 110, 110, "Adaptability", ["Tackle"], [], 300)
    opponent = Flygon("Flygon", 200, "Dragon", 100, 100, "Levitate", ["Dragon_Claw", "Fire_Blast", "Dragon_Dance", "Giga_Drain"], [], 200)

    # Simulate the battle
    while player.getHealth() > 0 and opponent.getHealth() > 0:
        print(f"{player.getName()} has {player.getHealth()} health.")
        print(f"{opponent.getName()} has {opponent.getHealth()} health.")
        
        # Player's turn
        move = int(input(f"It is {player.getName()}'s turn! Press 1 for Tackle: "))
        if move == 1:
            player.Tackle(opponent)
        
        # Check if opponent is defeated
        if opponent.getHealth() <= 0:
            print(f"{opponent.getName()} fainted! {player.getName()} wins!")
            break
        
        # Opponent's turn
        opponent_move = random.choice(opponent.getMoves())
        if opponent_move == "Dragon_Claw":
            opponent.Dragon_Claw(player)
        elif opponent_move == "Fire_Blast":
            opponent.Fire_Blast(player)
        elif opponent_move == "Dragon_Dance":
            opponent.Dragon_Dance()
        elif opponent_move == "Giga_Drain":
            opponent.Giga_Drain(player)
        
        # Check if player is defeated
        if player.getHealth() <= 0:
            print(f"{player.getName()} fainted! {opponent.getName()} wins!")
            break

    print("Battle over.")

# Example usage:
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
