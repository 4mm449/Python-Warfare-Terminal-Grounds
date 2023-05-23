import random
class Character:
    def __init__(self, name, profession, unit):
        self.attrib = {
            "Name" : name,
            "Profession": profession,
            "HP" : 100,
            "ATK" : 0,
            "DEF" : 0,
            "EXP" : 0,
            "Level" : 1,
            "Rank" : "Bronze" 
        }
        self.UNIT = unit
        # self.name = name
        # self.profession = profession
        # self.HP = 100
        # self.ATK = 0
        # self.DEF = 0
        # self.EXP = 0
        # self.LEVEL = 1
        # self.RANK = "Bronze"
        # self.UNIT = unit
        
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
            # f"\nPlayer Unit {self.UNIT}: "\
            # "\n---------------------------"\
            "\n(1) Name: ", self.attrib["Name"],\
            "\n(2) Profession: ",self.attrib["Profession"],\
            "\n(3) Health Point (HP): ",self.attrib["HP"],\
            "\n(4) Attack Point (ATK): ",self.attrib["ATK"],\
            "\n(5) Defence Point (DEF): ",self.attrib["DEF"],\
            "\n(6) Experience (EXP): ",self.attrib["EXP"],\
            "\n(7) Rank: ", self.attrib["Rank"],
            "\n---------------------------\n")
    def __str__(self) -> str:
        return "Name: {Name}, Profession: {Profession}, HP: {HP}, ATK: {ATK}, DEF: {DEF}, EXP: {EXP}, Rank: {Rank}" .format(**self.attrib)
        # return f"{{'Name': '{self.name}','Profession': '{self.profession}', 'HP': {self.HP}, 'ATK': {self.ATK}, DEF: {self.DEF}, EXP: {self.EXP}, Rank: '{self.RANK}'}}"
    # setting up warrior
    def setup_warrior(self):
        self.attrib["ATK"] = random.randint(5, 20)
        self.attrib["DEF"] = random.randint(1,20)
        self.attrib["Profession"] = 'Warrior'
        
    # setting up tanker
    def setup_tanker(self):
        self.attrib["ATK"] = random.randint(1, 10)
        self.attrib["DEF"] = random.randint(5, 15)
        self.attrib["Profession"] = 'Tanker'

        
    # defining the attack logic
    def attack(self, target):
        damage = self.ATK - target.DEF + random.randint(-5, 10)
        target.HP -= damage
        print(f"{self.name} attacked {target.name} and dealt {damage} damage")

    
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
