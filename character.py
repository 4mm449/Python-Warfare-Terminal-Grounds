import random
class Character:
    def __init__(self, name, profession, unit):
        self.name = name
        self.profession = profession
        self.HP = 100
        self.ATK = 0
        self.DEF = 0
        self.EXP = 0
        self.LEVEL = 1
        self.RANK = "Bronze"
        self.UNIT = unit
        
        # player chooses warrior
        if profession == 'W':
            self.setup_warrior()
        # player chooses warrior
        elif profession == 'T':
            self.setup_tanker()
        else:
            print("[-] ERROR. INVALID INPUT. Please enter W for Warrior and T for Tanker [-]")
        # display the stats
        print("---------------------------"\
            f"\nPlayer Unit {self.UNIT}: "\
            "\n---------------------------"\
            "\n(1) Name: ", self.name,\
            "\n(2) Profession: ",self.profession,\
            "\n(3) Health Point (HP): ",self.HP,\
            "\n(4) Attack Point (ATK): ",self.ATK,\
            "\n(5) Defence Point (DEF): ",self.DEF,\
            "\n(6) Experience (EXP): ",self.EXP,\
            "\n(7) Rank: ", self.RANK,
            "\n---------------------------\n")
    def __str__(self) -> str:
        return f"Name: {self.name}, Profession: {self.profession}, HP: {self.HP}, ATK: {self.ATK}, DEF: {self.DEF}, EXP: {self.EXP}, Rank: {self.RANK}"
    # setting up warrior
    def setup_warrior(self):
        self.ATK = random.randint(5, 20)
        self.DEF = random.randint(1,20)
        self.profession = 'Warrior'
        
    # setting up tanker
    def setup_tanker(self):
        self.ATK = random.randint(1, 10)
        self.DEF = random.randint(5, 15)
        self.profession = 'Tanker'

        
    # defining the attack logic
    def attack(self, target):
        damage = self.ATK - target.DEF + random.randint(-5, 10)
        target.HP -= damage
        print(f"{self.name} attacked {target.name} and dealt {damage} damage")

    # main battle
    def game(self):
        game_over = True
        try_again = True
        while game_over:
            while try_again:
                if self.HP == 100:
                    print("100")   
# player unit        
class Player:
    def __init__(self):
        self.units = []
        
    def add_unit(self, unit):
        self.units.append(unit)
        
    def remove_unit(self, unit):
        self.units.remove(unit)

# ai unit
class AI:
    def __init__(self):
        self.units = []
        
    def add_unit(self, unit):
        self.units.append(unit)
        
    def remove_unit(self, unit):
        self.units.remove(unit)
