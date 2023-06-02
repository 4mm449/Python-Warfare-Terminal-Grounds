import random
class Character:
    def __init__(self, name, profession, unit):
        self.attrib = {
            "Name": name,
            "Profession": profession,
            "HP": 100,
            "ATK": random.randint(10, 20),
            "DEF": random.randint(5, 10),
            "EXP": 0,
            "Level": 1,
            "Rank": "Bronze",
        }
        self.unit = unit
        # self.coins = 0
     # player chooses warrior
        if profession == 'W':
            self.setup_warrior()
    # player chooses warrior
        elif profession == 'T':
            self.setup_tanker()
    
    # setting up warrior
    def setup_warrior(self):
        self.attrib["ATK"] = random.randint(5, 20)
        self.attrib["DEF"] = random.randint(1, 10)
        self.attrib["Profession"] = 'Warrior'
        
    # setting up tanker
    def setup_tanker(self):
        self.attrib["ATK"] = random.randint(1, 10)
        self.attrib["DEF"] = random.randint(5, 15)
        self.attrib["Profession"] = 'Tanker'

    def __str__(self):
        return '''
(1) Name: {Name}
(2) Profession: {Profession}
(3) HP: {HP}
(4) ATK: {ATK}
(5) DEF: {DEF}
(6) EXP: {EXP}
(7) Rank: {Rank}
''' .format(**self.attrib)

#     def __str__(self):
# #         return '''
# :---------------------------------------------------------------------:
# | Unit Name     Profession    HP    ATK    DEF    EXP    Rank         |
# :---------------------------------------------------------------------:
# | {Name:<6}    {Profession:^12}    {HP:^4}    {ATK:^5}    {DEF:^5}    {EXP:^5}    {Rank:^6} |
# '---------------------------------------------------------------------'

# ''' .format(**self.attrib)
#         def __str__(self):
#             return '''
# .--------.--------------.------.-------.-------.-------.--------.
# |  Name  |  Profession  |  HP  |  ATK  |  DEF  |  EXP  |  Rank  |
# :--------+--------------+------+-------+-------+-------+--------:
# | {Name} | {Profession} | {HP} | {ATK} | {DEF} | {EXP} | {Rank} |
# '--------'--------------'------'-------'-------'-------'--------'
# '''.format(**self.attrib)

class Player:
    def __init__(self):
        self.units = []
        self.coins = 0
        

    def add_unit(self, unit):
        self.units.append(unit)
    def remove_unit(self, unit):
        self.units.remove(unit)
    

    



class AI:
    def __init__(self):
        self.units = []
        self.coins = 0
        
    def add_unit(self, unit):
        self.units.append(unit)

    def remove_unit(self, unit):
        self.units.remove(unit)
