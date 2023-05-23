import character
import random
import os
from sys import platform
if platform == "win32":
    import winsound

RANK = ["Bronze", "Silver", "Gold", "Diamond"]

def main():
    opsystem("win.mp3")
    game_intro()
    global player
    global ai
    player = character.Player()
    ai = character.AI()
    rounds = 1

    
    # Prompt user for player unit details and setup player units
    
    for i in range(3):
        unit_check = True
        while unit_check:
            name = input(f"(1) Enter the name for Unit {i + 1}: ")
            if name == "":
                print("[-] ERROR. Please specify a name for the unit. You cannot leave this field blank")
                unit_check = True
            else:   
                unit_check = False
                
        profession = input(f"(2) Choose either (W)arrior or (T)anker for Unit {i + 1}: ")
        profession_check = True
        

        while profession_check:
            try:
                if profession[0].upper() == 'W' or profession[0].upper() == 'T':
                    profession = profession[0].upper() 
                    unit = character.Character(name, profession, i + 1)
                    
                    print(f'''
---------------------------
Player Unit {i + 1}:
---------------------------
{unit}
---------------------------
                    ''')
                        
                    player.add_unit(unit)
                    profession_check = False
                else:
                    profession = input(f"[-] ERROR, BAD INPUT. Enter W for Warrior or T for Tanker for Unit {i + 1}: ")
            except:
                profession = input("[-] ERROR. No value specified. Please specify a value [W/T]: ")

        


    # Setup AI units
    for i in range(3):
        name = f"AI{random.randint(1, 99)}"
        profession = random.choice(["W", "T"])
        unit = character.Character(name, profession, i + 1)
        ai.units.append(unit)
        print(f'''
---------------------------
AI Unit {i + 1}:
---------------------------
{unit}
---------------------------
              ''')

    try_again = True
    game_over = False
    
    while game_over == False:
        # if rounds % 2 == 1:
        while try_again:
            # if rounds % 2 == 1:
            #     print(f"It's {player_name}'s turn to attack")
            #     display_stats(player.units, ai.units)
            #     attacker = input("Enter unit that you wish to send for an attack [1-3]: ")
            #     victim = input("Enter AI unit that you wish to attack [1-3]: ")
            # else:
            #     print("It's AI's turn to attack")
            #     attacker = random.choice(ai.units)
            #     victim = random.choice(player.units)
    
            
            print(f"It's {player_name}'s turn to attack")
            # display_stats(player.units, ai.units)
            stats_check = True
            while stats_check:
                attacker = input("Enter unit that you wish to send for an attack [1-3] or type U to check unit stats: ")
                try:
                    
                    if attacker.upper() == "U":
                        #display game stats
                        display_stats(player.units, ai.units)
                        attacker = input("Enter unit that you wish to send for an attack [1-3]: ")
                        victim = input("Enter AI unit that you wish to attack [1-3]: ")
                        stats_check = False
                    # elif int(attacker) > len(player.units):
                    #     print('[-] ERROR. There is no unit {attacker} present. Please check all available units by entering "U"')
                    #     try_again = True
                    else:
                        stats_check = False
                        victim = input("Enter AI unit that you wish to attack [1-3]: ")
                    if attacker == '' or victim == '':
                        attacker = input("[-] ERROR. No value specified. Please specify a value [1-3 or U]: ")
                        try_again = True
                    # elif int(attacker) not in [1, 2, 3] or int(victim) not in [1, 2, 3]:
                    #     try_again = True
                    # else:
                    #     try_again = True
                    #     print("[-] ERROR. Invalid Input, Please try again")
                        
                except:
                    attacker = input("[-] ERROR. No value specified. Please specify a value [1-3 or U]: ")
                    try_again = True
                # except ValueError:
                #     attacker = input("[-] ERROR. No value specified. Please specify a value [1-3 or U]: ")
                #     try_again = True
                    
            # try:
                
            attacker = int(attacker) - 1
            victim = int(victim) - 1
            try:
                if attacker in range(len(player.units)) and victim in range(len(ai.units)):
                    try_again = False
                    attack(player.units[attacker], ai.units[victim])
                    # attacker_unit = player.units[attacker]
                    # attacker_HP = int(attacker_unit["HP"])
                    # victim_unit = ai.units[victim]
                    # victim_HP = int(victim_unit["HP"])
                    print(f'''
---------------------------
Player Unit {attacker + 1}:          
---------------------------                     
{player.units[attacker]}

---------------------------
''')
                
                    print(f'''
---------------------------
AI Unit {victim + 1}:            
---------------------------                     
{ai.units[victim]}
---------------------------
''')
                else:
                    attacker = print("[-] ERROR. Invalid unit selection. Please try again. [-]")
                    try_again + True
            
            except IndexError:
                print("")
               
                
            # else:   
            #     print('[-] ERROR. There is no unit {attacker} present. Please check all available units by entering "U"')
            #     try_again = True
                    # bonus_exp(victim)
               
            
            # except ValueError:
            #         print("[-] ERROR. Invalid input. Please enter a number. [-]")
            # except IndexError:
            #         print("[-] ERROR. The AI unit that you selected has already been defeated. Please enter another unit [-]")
        
            
        # elif:
        # AI chooses to attack 

        if len(ai.units) > 0:
            input("It's AI's turn to attack. Press return (enter) to continue...")
            attacker = random.choice(ai.units)
            victim = random.choice(player.units)
            attack(attacker, victim)
        # bonus_exp(victim)
                
            try_again = True
        else:
            pass
        
        


               

            # rounds += 1
            # try_again = True
        game_over = is_game_over(player.units, ai.units)

def bonus_exp(victim):
        #bonus EXP points
        #Player gives more than 10 damage to AI, gets 20% more EXP
        #Player gives less than 0 damage to AI, gets 50% more EXP, if negative, brings  the EXP down
        if  damage > 10:
            victim["EXP"] += (0.2 * damage)
        elif damage <= 0:
            victim["EXP"] += (0.5 * damage)

def attack(attacker, victim):
    global damage
    
    # print(f"\n{attacker.attrib['Name']} is attacking {victim.attrib['Name']}")
    # damage = attacker.attrib["ATK"] - victim.attrib["DEF"]
    # if damage > 0:
    #     victim.attrib["HP"] -= damage
    #     print(f"{victim.attrib['Name']} received {damage} damage.")
    #     if victim.attrib["HP"] <= 0:
    #         print(f"{victim.attrib['Name']} has been defeated.")
    # else:
    #     print(f"The attack was ineffective. No damage was dealt.")

    print(f"\n{attacker.attrib['Name']} is attacking {victim.attrib['Name']}!\n")
    # damage = max(0, attacker.attrib["ATK"] - victim.attrib["DEF"])
    os.system("afplay slash.mp3&")
    # Calculate damage
    randomatkpt = random.randint(-5, 10)
    damage = attacker.attrib["ATK"] - victim.attrib["DEF"] + randomatkpt
    # if attacker.attrib["ATK"] < victim.attrib["DEF"] and randomatkpt < 0:
    #     damage = attacker.attrib["ATK"] - victim.attrib["DEF"] - randomatkpt
    victim.attrib["HP"] -= damage
    # Calculate EXP
    attacker.attrib["EXP"] += damage
    victim.attrib["EXP"] += victim.attrib["DEF"]
    # HP below 100, normal behaviour
    if victim.attrib["HP"] <= 100:
        print("{Name} takes " .format(**victim.attrib), end='')
        print(f"{damage} damage.\n")
    # HP never goes above 100
    elif victim.attrib["HP"] > 100:
        print("{Name} takes " .format(**victim.attrib), end='')
        print(f"0 damage.\n")
        victim.attrib["HP"] = 100
    if victim.attrib["HP"] <= 0:
        print("{Name} has been defeated!" .format(**victim.attrib))
        os.system("afplay unit_dead.wav&")
        if victim in player.units:
            player.units.remove(victim)
        elif victim in ai.units:
            ai.units.remove(victim)
    else:
        print("{Name} has {HP} HP remaining." .format(**victim.attrib))
    
    # Bonus EXP points
    if damage > 10:
        victim.attrib["EXP"] += int(0.2 * damage)
    elif damage <= 0:
        victim.attrib["EXP"] += int(0.5 * damage)
    
    # Promotion logic - attacker
    if attacker.attrib["EXP"] >= 100:
        attacker.attrib["EXP"] -= 100
        attacker.attrib["Level"] += 1
        if attacker.attrib["Level"] == 2:
                attacker.attrib["Rank"] = RANK[1]
        elif attacker.attrib["Level"] == 3:
            attacker.attrib["Rank"] = RANK[2]  
        elif attacker.attrib["Level"] == 4:
                attacker.attrib["Rank"] = RANK[3]  
        # attacker. = attacker.attrib["Rank"]
        # print(f"[+] EXP -100, Player Unit {attacker +1}: ", end='')
        print("\n[+] EXP -100, {Profession} {Name} has been promoted to {Rank}. Press return to continue..." .format(**attacker.attrib), end='')
        os.system("afplay level_up.wav&")
    
    # Promotion logic - victim
    elif victim.attrib["EXP"] >= 100:
        victim.attrib["EXP"] -= 100
        victim.attrib["Level"] += 1
        if victim.attrib["Level"] == 2:
                victim.attrib["Rank"] = RANK[1]
        elif victim.attrib["Level"] == 3:
            victim.attrib["Rank"] = RANK[2]  
        elif victim.attrib["Level"] == 4:
                victim.attrib["Rank"] = RANK[3]  
        # victim. = victim.attrib["Rank"]
        # print(f"[+] EXP -100,  Unit {victim +1}: ", end='')
        print("\n[+] EXP -100, {Profession} {Name} has been promoted to {Rank}. Press return to continue..." .format(**victim.attrib), end='')
        os.system("afplay level_up.wav&")
        


    print("\n-----------------------------------\n")


def is_game_over(player_units, ai_units):
    if all(unit.attrib["HP"] <= 0 for unit in player_units):
        print("AI wins! Game over.")
        return True
    elif all(unit.attrib["HP"] <= 0 for unit in ai_units):
        print(f"{player_name} wins! Congratulations!")
        os.system("afplay win.mp3&")
        return True
    else:
        return False


def display_stats(player_units, ai_units):
    print("\n------- Player Units -------")
    for i, unit in enumerate(player_units):
        # print(f"{i+1}. {unit}: HP={unit.attrib['HP']} ATK={unit.attrib['ATK']} DEF={unit.attrib['DEF']}")
         print(f'''
--------------------------
Player Unit {i+1}:
--------------------------
{unit}
--------------------------
              ''')
        # print(f"Player Unit {i+1}:\n {unit}")
        # print("--------------------------\n")
    print("\n------- AI Units -------")
    for i, unit in enumerate(ai_units):
        # print(f"{i+1}. {unit}: HP={unit.attrib['HP']} ATK={unit.attrib['ATK']} DEF={unit.attrib['DEF']}")
        print(f'''
--------------------------
AI Unit {i+1}:
--------------------------
{unit}
--------------------------
              ''')
        # print(f"AI Unit {i+1}:\n {unit}\n")
        # print("--------------------------\n")

    # print("\n-----------------------------------\n")
def opsystem(audio: str):
    if platform == "linux" or platform == "linux2":
        os.system(f"aplay {audio}&")
        # print("Linux")
        # linux
    elif platform == "darwin":
        # print("MacOS")
        os.system(f"afplay {audio}&")
        # OS X
    elif platform == "win32":
        winsound.PlaySound(f"{audio}", winsound.SND_ASYNC)
        # print("Windows")
        # Windows...
    else:
        print("Sorry, sound for your operating system is not supported yet")
        
    
def progress_bar(value):
    zerototen = f'''
    █▒▒▒▒▒▒▒▒▒ {value}
    '''
    tentotwenty = f'''
    ██▒▒▒▒▒▒▒▒ {value}
    '''
    twentytothirty = f'''
    ███▒▒▒▒▒▒▒ {value}
    '''
    thirtytoforty = f'''
    ████▒▒▒▒▒▒ {value}
    '''
    fortytofifty = f'''
    █████▒▒▒▒▒ {value}
    '''
    fiftytosixty = f'''
    ██████▒▒▒▒ {value}
    '''
    sixtytoseventy = f'''
    ███████▒▒▒ {value}
    '''
    seventytoeighty = f'''
    ████████▒▒ {value}
    '''
    eightytoninety = f'''
    █████████▒ {value}
    '''
    ninetytohundred = f'''
    ██████████ {value}
    '''
    if value > 0 and value <= 10:
        print(zerototen)
    elif value > 10 and value <= 20:
        print(tentotwenty)
    elif value > 20 and value <= 30:
        print(twentytothirty)
    elif value > 30 and value <= 40:
        print(thirtytoforty)
    elif value > 40 and value <= 50:
        print(fortytofifty)
    elif value > 50 and value <= 60:
        print(fiftytosixty)
    elif value > 60 and value <= 70:
        print(sixtytoseventy)
    elif value > 70 and value <= 80:
        print(seventytoeighty)
    elif value > 80 and value <= 95:
        print(eightytoninety)
    elif value > 95 and value == 100:
        print(ninetytohundred)

def game_intro():
#     banner_text = '''                                            
#  _____     _   _   _        _____             _     
# | __  |___| |_| |_| |___   | __  |___ _ _ ___| |___ 
# | __ -| .'|  _|  _| | -_|  |    -| . | | | .'| | -_|
# |_____|__,|_| |_| |_|___|  |__|__|___|_  |__,|_|___|
#                                      |___|          
#     '''

    banner_text = '''
  ___      _   _              __      __         __              
 | _ \_  _| |_| |_  ___ _ _   \ \    / /_ _ _ _ / _|__ _ _ _ ___ 
 |  _/ || |  _| ' \/ _ \ ' \   \ \/\/ / _` | '_|  _/ _` | '_/ -_)
 |_|  \_, |\__|_||_\___/_||_|   \_/\_/\__,_|_| |_| \__,_|_| \___|
      |__/                                                       
                               
                                 _ 
                                (_)
                                 _ 
                                (_)


  _____              _           _    ___                      _    
 |_   _|__ _ _ _ __ (_)_ _  __ _| |  / __|_ _ ___ _  _ _ _  __| |___
   | |/ -_) '_| '  \| | ' \/ _` | | | (_ | '_/ _ \ || | ' \/ _` (_-<
   |_|\___|_| |_|_|_|_|_||_\__,_|_|  \___|_| \___/\_,_|_||_\__,_/__/                                                                                                                                                                                                                      
'''

    print(banner_text)
    print("Welcome to Python Warfare : Terminal Grounds Turn-Based Battle game!")
    global player_name
    name_check = True
    while name_check:
        player_name = input("What is your name? ")
        if player_name == "":
            print("[-] ERROR. Please specify a name. You cannot leave this field blank")
            name_check = True
        else:
            print(f"\nHello {player_name}\n")
            name_check = False
        
    print(f"Okay! let's play, {player_name}! This game allows you to setup a team which is made up of 3 units. The characters available to fill up your 3 units can ONLY be either a (W)arrior or a (T)anker.")
    print(f"Each unit has a:\n(1) Name\n(2) Health Point (HP)\n(3) Attack Point (ATK)\n(4) Defence Point (DEF)\n(5) Experience (EXP)\n(6) Rank: {RANK[0]} | {RANK[1]} | {RANK[2]} | {RANK[3]}")
    cont = input("\nEnter I for instructions or Press return to continue: ")
    if cont.upper() == "I":
        print("Instructions:")
        print("1. Each player takes turns attacking.")
        print("2. You will be prompted to select one of your units to attack with, and then choose the AI's unit to attack.")
        print("3. Damage dealt is calculated based on the attacker's attack points and the defender's defense points.")
        print("4. The game continues until all units from one side are defeated.")
        print("5. Good luck and have fun!\n")
    else:
        pass

    # return init2, init3, init4, init5, init6


game_over = False
rounds = 1

if __name__ == "__main__":
    main()
