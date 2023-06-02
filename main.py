# -----------------------------------------------------------------------------
# Title: Python Warfare : Terminal Grounds
# Authors: Group 1: Ammaar, Abdullah, Thaha, Santosh, Fadly, Anh 
# Date: 01/05/2023
# Link to Git repository: https://github.com/4mm449/battle_royale
# -----------------------------------------------------------------------------



import character
import random
import os
from sys import platform
import datetime
try:
  from tabulate import tabulate
except ImportError:
  print("Trying to Install required module: tabulate\n")
  os.system('python -m pip install tabulate')
# above lines try to install tabulate module if not present
# if all went well, import required module again (for global access)
# from tabulate import tabulate

# to check and import winsound module so that program doesnt crash on mac and linux
if platform == "win32":
    import winsound


# initialising all global variables
log_file_name = f"logs_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt" # introducing what the logs filename would be
inp = 'inp' # value for log function below
out = 'out' # value for log function below
UNITS = 3
RANK = ["Bronze", "Silver", "Gold", "Diamond"] # 4 different levels

# main game function
def main():
    print(f"\nLog file for this game will be saved at logs/{log_file_name}")
    opsystem("audio/intro.wav")
    game_intro()
    global player
    global ai
    player = character.Player()
    ai = character.AI()

    
    # Prompt user for player unit details and setup player units
    
    for i in range(UNITS):
        unit_check = True
        while unit_check:
            name = input(f"(1) Enter the name for Unit {i + 1}: ")
            log(f"(1) Enter the name for Unit {i + 1}: ", out)
            
            if name == "":
                print("[-] ERROR. Please specify a name for the unit. You cannot leave this field blank")
                unit_check = True
            else:   
                unit_check = False
            log(name, inp)    
        profession = input(f"(2) Choose either (W)arrior or (T)anker for Unit {i + 1}: ")
        log(f"(2) Choose either (W)arrior or (T)anker for Unit {i + 1}: ", out)
        profession_check = True
        

        while profession_check:
            try:
                if profession[0].upper() == 'W' or profession[0].upper() == 'T':
                    profession = profession[0].upper() 
                    unit = character.Character(name, profession, i + 1)
                    log(profession, inp)
                    
                    
#                     print(f'''
# ---------------------------
# Player Unit {i + 1}:
# ---------------------------
# {unit}
# ---------------------------
#                     ''')
#                     log(f'''
# ---------------------------
# Player Unit {i + 1}:
# ---------------------------
# {unit}
# ---------------------------
#                     ''', out)
                    print(f"\nPlayer Unit {i + 1}:")
                    player_table = []
                    player_table.append([
                    # f"Player Unit {i+1}",
                    unit.attrib["Name"],
                    unit.attrib["Profession"],
                    # progress_bar(unit.attrib["HP"], "HP"),
                    unit.attrib["HP"],
                    unit.attrib["ATK"],
                    unit.attrib["DEF"],
                    unit.attrib["EXP"],
                    unit.attrib["Rank"]
                    ])
                    print(tabulate(player_table, headers=["Name", "Profession", "HP", "ATK", "DEF", "EXP", "Rank"], tablefmt="fancy_grid"))

                    player.add_unit(unit)
                    profession_check = False
                else:
                    profession = input(f"[-] ERROR, BAD INPUT. Enter W for Warrior or T for Tanker for Unit {i + 1}: ")
                    log(f"[-] ERROR, BAD INPUT. Enter W for Warrior or T for Tanker for Unit {i + 1}: ", out)
                    log(profession, inp)
            except:
                profession = input("[-] ERROR. No value specified. Please specify a value [W/T]: ")
                log("[-] ERROR. No value specified. Please specify a value [W/T]: ", out)
                log(profession, inp)
                
        


    # Setup AI units
    for i in range(3):
        name = f"AI{random.randint(1, 99)}"
        profession = random.choice(["W", "T"])
        log(f"AI chooses {profession}", out)
        unit = character.Character(name, profession, i + 1)
        ai.units.append(unit)
#         print(f'''
# # ---------------------------
# # AI Unit {i + 1}:
# # ---------------------------
# # {unit}
# # ---------------------------
# #               ''')
# #         log(f'''
# # ---------------------------
# # AI Unit {i + 1}:
# # ---------------------------
# # {unit}
# # ---------------------------
# #               ''', out)
        ai_table = []
        print(f"\nAI Unit {i + 1}:")
        ai_table.append([
                    # f"AI Unit {i+1}",
                    unit.attrib["Name"],
                    unit.attrib["Profession"],
                    # progress_bar(unit.attrib["HP"], "HP"),
                    unit.attrib["HP"],
                    unit.attrib["ATK"],
                    unit.attrib["DEF"],
                    unit.attrib["EXP"],
                    unit.attrib["Rank"]
                ])
        print(tabulate(ai_table, headers=["Name", "Profession", "HP", "ATK", "DEF", "EXP", "Rank"], tablefmt="fancy_grid"))
# def display_stats(player_units, ai_units):

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
    
            
            print(f"\nIt's {player_name}'s turn to attack")
            log(f"\nIt's {player_name}'s turn to attack", out)
            # print(f"{player_name} has {player.coins} coins")
            # display_stats(player.units, ai.units)
            
            stats_check = True
            # while stats_check:
            #     # attacker = input(f"Enter unit that you wish to send for an attack [1-{len(player.units)}]  type U or to check unit stats or type S to access : ")
            #     attacker = input(f"Options: \nEnter unit that you wish to send for an attack [1-{len(player.units)}]\nDisplay (U)nits [U]\nAccess the (P)ystore [P]\nPlease choose one of the options [1-{len(player.units)}], U or P: ")
            #     log(f"Enter unit that you wish to send for an attack [1-{len(player.units)}] or type U to check unit stats: ", out)
            #     log(attacker, inp)

            #     if attacker.upper() == "U":
            #         # Display game stats
            #         display_stats(player.units, ai.units)
            #         attacker = input(f"Enter unit that you wish to send for an attack [1-{len(player.units)}]: ")
            #         log(f"Enter unit that you wish to send for an attack [1-{len(player.units)}]: ", out)
            #         log(attacker, inp)
            #     elif attacker.upper() == "P":
            #         coin_store(player)
                    
            #     if attacker.isdigit() and int(attacker) in range(1, 4):
            #         stats_check = False
            #     else:
            #         print(f"[-] ERROR. Invalid input. Please enter a valid option [1-{len(player.units)}], U or P]")

            # stats_check = True
            # while stats_check:
            #     victim = input(f"Enter AI unit that you wish to attack [1-{len(ai.units)}]: ")
            #     log(f"Enter AI unit that you wish to attack [1-{len(ai.units)}]: ", out)
            #     log(victim, inp)

            #     if victim.isdigit() and int(victim) in range(1, 4):
            #         stats_check = False
            #     else:
            #         print(f"[-] ERROR. Invalid input. Please enter a valid option [1-{len(ai.units)}]")
            #         log(f"[-] ERROR. Invalid input. Please enter a valid option [1-{len(player.units)}]", out)
            while stats_check:
                if mode[0].upper() == 'N':
                    # Determine the suggested unit to choose
                    suggested_unit = max(player.units, key=lambda unit: unit.attrib["ATK"])

                    # Determine the suggested AI unit to attack
                    suggested_target = min(ai.units, key=lambda unit: (unit.attrib["DEF"], unit.attrib["HP"]))

                    # Print the suggestions
                    print(f"\nPybot suggests you to attack with Player Unit {player.units.index(suggested_unit) + 1}")
                    print(f"Pybot suggests you to attack AI Unit {ai.units.index(suggested_target) + 1}\n")
                attacker = input("\nOptions:\n"
                                f"• Enter unit that you wish to send for an attack [1-{len(player.units)}]\n"
                                "• Display (U)nits [U]\n"
                                "• Access the (P)ystore [P]\n"
                                f"Please choose one of the options [1-{len(player.units)}], U or P: ")
                log(f"Enter unit that you wish to send for an attack [1-{len(player.units)}] or type U to check unit stats: ", out)
                log(attacker, inp)

                if attacker.upper() == "U":
                    # Display game stats
                    display_stats(player.units, ai.units)
                    continue  # Restart the loop to prompt for input again

                if attacker.upper() == "P":
                    coin_store(player)
                    continue  # Restart the loop to prompt for input again

                if attacker.isdigit() and int(attacker) in range(1, len(player.units) + 1):
                    stats_check = False
                else:
                    print(f"\n[-] ERROR. Invalid input. Please enter a valid option [[1-{len(player.units)}], U or P]")

            stats_check = True
            while stats_check:
                victim = input(f"Enter AI unit that you wish to attack [1-{len(ai.units)}]: ")
                log(f"Enter AI unit that you wish to attack [1-{len(ai.units)}]: ", out)
                log(victim, inp)

                if victim.isdigit() and int(victim) in range(1, len(ai.units) + 1):
                    stats_check = False
                else:
                    print(f"\n[-] ERROR. Invalid input. Please enter a valid option [1-{len(ai.units)}]")
                    log(f"\n[-] ERROR. Invalid input. Please enter a valid option [1-{len(ai.units)}]", out)

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
                    
                    attackerhp = progress_bar(player.units[attacker].attrib["HP"], "HP")
                    victimhp = progress_bar(ai.units[victim].attrib["HP"], "HP")
                    coins_indication = progress_bar(player.coins, "Pycoins")
                    print("\n")
                    team_strength_value = team_strength(player)
                    team_strength_text = f"Team Strength: {team_strength_value:.2f}"
                    print(team_strength_text)
                    print(coins_indication)
                    print(f'''
----------------------------------
 Player Unit {attacker + 1}: {attackerhp}
----------------------------------''', end='')  
                    print(f'''                               
{player.units[attacker]}
----------------------------------
''')
                    log(f'''
----------------------------------
 Player Unit {attacker + 1}: {attackerhp}
----------------------------------''', out)  
                    log(f'''                               
{player.units[attacker]}
----------------------------------
''', out)
                    coinsl(player)

#                     print(f'''
# ---------------------------
# Player Unit {attacker + 1}:           
# ---------------------------                     
# {player.units[attacker]}

# ---------------------------
# ''')
                
#                     print(f'''
# ----------------------------------
# AI Unit {victim + 1}:            
# ----------------------------------                     
# {ai.units[victim]}
# ---------------------------
# ''')
                    coins_indication = progress_bar(ai.coins, "Pycoins")
                    print("\n")
                    team_strength_value = team_strength(ai)
                    team_strength_text = f"Team Strength: {team_strength_value:.2f}"
                    print(team_strength_text)
                    print(coins_indication)
                    print(f'''
----------------------------------
 AI Unit {victim + 1}:     {victimhp}
----------------------------------''', end='')  
                    print(f'''                               
{ai.units[victim]}
----------------------------------
''')
                    log(f'''
----------------------------------
 AI Unit {victim + 1}:     {victimhp}
----------------------------------''', out)  
                    log(f'''                               
{ai.units[victim]}
----------------------------------
''', out)
                else:
                    #  attacker = input("[-] ERROR. Invalid unit selection. Please try again. [-]")
                    print("[-] ERROR. Invalid unit selection. Please try again. [-]")
                    log("[-] ERROR. Invalid unit selection. Please try again. [-]", out)
                    log(attacker, inp)
                    try_again = True
            
            except IndexError:
                pass
               
                
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
        if mode[0].upper() == 'N' or mode[0].upper() == 'I':
            if len(ai.units) > 0:
                input("It's AI's turn to attack. Press return (enter) to continue...")
                log("It's AI's turn to attack. Press return (enter) to continue...", out)
                
                # basic AI algorithm
                attacker = random.choice(ai.units)
                victim = random.choice(player.units)
                attack(attacker, victim)
                coinsl(ai)
                
                try_again = True
                
                    
        elif mode[0].upper() == 'P':      
            if len(ai.units) > 0:
                input("It's AI's turn to attack. Press return (enter) to continue...")
                log("It's AI's turn to attack. Press return (enter) to continue...", out)
                
                # Determine the attacker
                # Choose the target
                # Execute the attack
                # advanced AI algorithm
                attacker = max(ai.units, key=lambda unit: unit.attrib["ATK"])
                victim = min(player.units, key=lambda unit: unit.attrib["DEF"])
                attack(attacker, victim)
                coinsl(ai)
        
                try_again = True
                
        if ai.coins >= 50:
            coin_store(ai)

        
            

        
            
        
        



        game_over = is_game_over(player.units, ai.units)
        file.close()
        
def team_strength(team):
    total_strength = sum(unit.attrib["ATK"] + unit.attrib["DEF"] + unit.attrib["HP"] for unit in team.units)
    normalized_strength = total_strength / len(team.units)
    team_strength = normalized_strength * 200 / 300  # Scale the strength to the range 1-200
    team_strength = max(1, min(200, team_strength))  # Clamp the value between 1 and 200
    return round(team_strength, 2)  # Return the team strength with 2 decimal places


def bonus_exp(victim):
        #bonus EXP points
        #Player gives more than 10 damage to AI, gets 20% more EXP
        #Player gives less than 0 damage to AI, gets 50% more EXP, if negative, brings  the EXP down
        if  damage > 10:
            victim["EXP"] += (0.2 * damage)
        elif damage <= 0:
            victim["EXP"] += (0.5 * damage)

# main battle logic
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
    print("\n-----------------------------------")
    print(f"\n{attacker.attrib['Name']} is attacking {victim.attrib['Name']}!\n")
    log(f"\n{attacker.attrib['Name']} is attacking {victim.attrib['Name']}!\n", out)
    # damage = max(0, attacker.attrib["ATK"] - victim.attrib["DEF"])
    opsystem("audio/slash.wav")
    # os.system("afplay slash.mp3&")
    # Calculate damage
    randomatkpt = random.randint(-5, 10)
    damage = attacker.attrib["ATK"] - victim.attrib["DEF"] + randomatkpt
    # coins   
    
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
            
        log("{Name} takes " .format(**victim.attrib), out)
        log(f"{damage} damage.\n", out)
    # HP never goes above 100
    elif victim.attrib["HP"] > 100:
        print("{Name} takes " .format(**victim.attrib), end='')
        print(f"0 damage.\n")
            
        log("{Name} takes " .format(**victim.attrib), out)
        log(f"0 damage.\n", out)
        victim.attrib["HP"] = 100
        
    if victim.attrib["HP"] <= 0:
        print("{Name} has been defeated!" .format(**victim.attrib))
        log("{Name} has been defeated!" .format(**victim.attrib), out)   
        # os.system("afplay unit_dead.wav&")
        if victim in player.units:
            opsystem("audio/player_dead.wav")
            player.units.remove(victim)
        elif victim in ai.units:
            opsystem("audio/unit_dead.wav")
            ai.units.remove(victim)

    else:
        print("{Name} has {HP} HP remaining." .format(**victim.attrib))
        log("{Name} has {HP} HP remaining." .format(**victim.attrib), out)

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
        opsystem("audio/level_up.wav")
        print("\n[+] EXP -100, {Profession} {Name} has been promoted to {Rank}." .format(**attacker.attrib))
        if attacker in player.units:
            choice = input("\n(1) Upgrade {Profession} {Name}s ATK by 1,\n(2) Upgrade {Profession} {Name}'s DEF by 1\nPlease choose an upgrade option [1-2]: ".format(**attacker.attrib))
            upgrade_check = True
            while upgrade_check:
                if choice == '1' or choice == '2':
                    if choice == '1':
                        attacker.attrib["ATK"] += 1
                        print("[+] {Profession} {Name}s ATK successfully increased by 1" .format(**attacker.attrib))
                        upgrade_check = False
                    elif choice == '2':
                        attacker.attrib["DEF"] += 1
                        print("[+] {Profession} {Name}s DEF successfully increased by 1".format(**attacker.attrib))
                        upgrade_check = False
                    elif choice == '':
                        choice = input("[-] ERROR. No value specified, Please try again [1-2]: ")
                        upgrade_check = True
                else:
                    choice = input("[-] Invalid Choice, Please try again [1-2]: ")
                    upgrade_check = True
        elif attacker in ai.units:
            options = [int(attacker.attrib["ATK"]), int(attacker.attrib["DEF"])]
            choice = random.choice(options)
            if choice == attacker.attrib["ATK"]:
                attacker.attrib["ATK"] += 1
                print("\n[+] {Profession} {Name}s ATK successfully increased by 1" .format(**attacker.attrib))
            elif choice == attacker.attrib["DEF"]:
                attacker.attrib["DEF"] += 1
                print("\n[+] {Profession} {Name}s ATK successfully increased by 1" .format(**attacker.attrib))
            
        
        log("\n[+] EXP -100, {Profession} {Name} has been promoted to {Rank}." .format(**attacker.attrib), out)
        
        # os.system("afplay level_up.wav&")

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
        opsystem("audio/level_up.wav")
        print("\n[+] EXP -100, {Profession} {Name} has been promoted to {Rank}." .format(**victim.attrib))
        if victim in player.units:
            choice = input("\n(1) Upgrade {Profession} {Name}'s ATK by 1,\n(2) Upgrade {Profession} {Name}'s DEF by 1\nPlease choose an upgrade option [1-2]: ".format(**victim.attrib))
            upgrade_check = True
            while upgrade_check:
                if choice == '1' or choice == '2':
                    if choice == '1':
                        victim.attrib["ATK"] += 1
                        print("\n[+] {Profession} {Name}s ATK successfully increased by 1" .format(**victim.attrib))
                        upgrade_check = False
                    elif choice == '2':
                        victim.attrib["DEF"] += 1
                        print("\n[+] {Profession} {Name}s DEF successfully increased by 1".format(**victim.attrib))
                        upgrade_check = False
                    elif choice == '':
                        choice = input("[-] ERROR. No value specified, Please try again [1-2]: ")
                        upgrade_check = True
                else:
                    choice = input("[-] ERROR. Invalid Choice, Please try again [1-2]: ")
                    upgrade_check = True
        elif victim in ai.units:
            options = [victim.attrib["ATK"], victim.attrib["DEF"]]
            choice = random.choice(options)
            if choice == victim.attrib["ATK"]:
                victim.attrib["ATK"] += 1
                print("\n[+] {Profession} {Name}s ATK successfully increased by 1" .format(**victim.attrib))
            elif choice == victim.attrib["DEF"]:
                victim.attrib["DEF"] += 1
                print("\n[+] {Profession} {Name}s ATK successfully increased by 1" .format(**victim.attrib))
        
        log("\n[+] EXP -100, {Profession} {Name} has been promoted to {Rank}." .format(**victim.attrib), out)
        
        # os.system("afplay level_up.wav&")
        


    print("\n-----------------------------------\n")

def coinsl(attacker):
    if damage > 0:
        coins = 2 * damage
        attacker.coins += coins
        if attacker.coins > 200:
            attacker.coins = 200

# check if all units are dead and check if the game is done
def is_game_over(player_units, ai_units):
    if all(unit.attrib["HP"] <= 0 for unit in player_units):
        print(f"{player_name} lost. Game over.")
        
        log(f"{player_name} lost. Game over.", out)
        opsystem("audio/lost.wav")
        return True
    elif all(unit.attrib["HP"] <= 0 for unit in ai_units):
        print(f"{player_name} wins! Congratulations!")
        
        log(f"{player_name} wins! Congratulations!", out)
        opsystem("audio/win.wav")
        # os.system("afplay win.mp3&")
        return True
    else:
        return False
    

# display all units on command
def display_stats(player_units, ai_units):
    print("\nPlayer Units\n")
    team_strength_value = team_strength(player)
    team_strength_text = f"Team Strength: {team_strength_value:.2f}"
    player_table = []
    for i, unit in enumerate(player_units):
        player_table.append([
            f"Player Unit {i+1}",
            unit.attrib["Name"],
            unit.attrib["Profession"],
            progress_bar(unit.attrib["HP"], "HP"),
            # unit.attrib["HP"],
            unit.attrib["ATK"],
            unit.attrib["DEF"],
            unit.attrib["EXP"],
            unit.attrib["Rank"]
        ])
    print(team_strength_text)
    coins_indication = progress_bar(player.coins, "Pycoins")
    # print("\n")
    print(coins_indication)
    # print("\n")
    print(tabulate(player_table, headers=["Unit", "Name", "Profession", "HP", "ATK", "DEF", "EXP", "Rank"], tablefmt="fancy_grid"))


    print("\nAI Units\n")
    team_strength_value = team_strength(ai)
    team_strength_text = f"Team Strength: {team_strength_value:.2f}"
    ai_table = []
    for i, unit in enumerate(ai_units):
        ai_table.append([
            f"AI Unit {i+1}",
            unit.attrib["Name"],
            unit.attrib["Profession"],
            progress_bar(unit.attrib["HP"], "HP"),
            # unit.attrib["HP"],
            unit.attrib["ATK"],
            unit.attrib["DEF"],
            unit.attrib["EXP"],
            unit.attrib["Rank"]
        ])
    print(team_strength_text)
    coins_indication = progress_bar(ai.coins, "Pycoins")
    # print("\n")
    print(coins_indication)
    # print("\n")
    print(tabulate(ai_table, headers=["Unit", "Name", "Profession", "HP", "ATK", "DEF", "EXP", "Rank"], tablefmt="fancy_grid"))
# def display_stats(player_units, ai_units):
#     print("\n---------- Player Units ----------")
#     # print("\n")
#     team_strength_value = team_strength(player)
#     border = "+" + "-" * 32 + "+"
#     text = f"Team Strength: {team_strength_value}".center(32)
#     output = f"{border}\n|{text}|\n{border}"
#     print(output)
#     coins_indication = progress_bar(player.coins, "Pycoins")
#     # print("\n")
#     print(coins_indication)
#     log("\n---------- Player Units ----------", out)
#     for i, unit in enumerate(player_units):
#         playerhp = progress_bar(unit.attrib["HP"], "HP")
#         # print(f"{i+1}. {unit}: HP={unit.attrib['HP']} ATK={unit.attrib['ATK']} DEF={unit.attrib['DEF']}")
        
#         print(f'''
# ----------------------------------
# Player Unit {i+1}: {playerhp}
# ----------------------------------
# {unit}
# ----------------------------------
#               ''')
        
#         log(f'''
# ----------------------------------
# Player Unit {i+1}: {playerhp}
# ----------------------------------
# {unit}
# ----------------------------------
#               ''', out)
#         # print(f"Player Unit {i+1}:\n {unit}")
#         # print("--------------------------\n")
#     print("\n------------ AI Units ------------")
#     # print("\n")
#     team_strength_value = team_strength(player)
#     border = "+" + "-" * 32 + "+"
#     text = f"Team Strength: {team_strength_value}".center(32)
#     output = f"{border}\n|{text}|\n{border}"
#     print(output)
#     coins_indication = progress_bar(ai.coins, "Pycoins")
#     # print("\n")
#     print(coins_indication)
#     log("\n------------ AI Units ------------", out)
#     for i, unit in enumerate(ai_units):
#         # print(f"{i+1}. {unit}: HP={unit.attrib['HP']} ATK={unit.attrib['ATK']} DEF={unit.attrib['DEF']}")
#         aihp = progress_bar(unit.attrib["HP"], "HP")
#         print(f'''
# ----------------------------------
# AI Unit {i+1}:     {aihp}
# ----------------------------------
# {unit}
# ----------------------------------
#               ''')
        
#         log(f'''
# ----------------------------------
# AI Unit {i+1}:     {aihp}
# ----------------------------------
# {unit}
# ----------------------------------
#               ''', out)
        # print(f"AI Unit {i+1}:\n {unit}\n")
        # print("--------------------------\n")

    # print("\n-----------------------------------\n")



# audio logic for different operating systems
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
        log("Sorry, sound for your operating system is not supported yet", out)
 

# logging logic
def log(event, inpout):
    # Define the log file name with the current date and time
    global file
    with open(f"logs/{log_file_name}", "a") as file:
        # current date and time
        # current_time = datetime.datetime.now()
        # file.write(f"{current_time}\n")
        if inpout == 'inp':
            file.write(f"> {event}\n")
        #logging
        elif inpout == 'out':
            file.write(f"{event}\n")
        # file.write(f"Details: {details}\n")
        # file.write("--------------------\n")   
            
def coin_store(visitor):
    if visitor == player:
        print("\nWelcome to the PyStore!")
        print(f"You have {visitor.coins} Pycoins.")
        print("------------------------")
        print("1. Buy Health Potion (100 Pycoins)")
        print("2. Buy Attack Boost (50 Pycoins)")
        print("3. Buy Defense Boost (50 Pycoins)")
        print("4. Exit Store")
        choice = input("Enter your choice [1-4]: ")
    else:
        if visitor.coins > 50 and visitor.coins < 100:
            choice = str(random.randint(2, 3))
        else:
            choice = str(random.randint(1, 3))
    if choice == "1":
        if visitor.coins >= 100 and visitor == player:
            valid = False
            while valid == False:
                chosen_unit = input(f"Which unit do you want to use the Health Potion on [1-{len(player.units)}]: ")
                if chosen_unit.isdigit() and 1 <= int(chosen_unit) <= len(player.units):
                    chosen_unit_index = int(chosen_unit) - 1
                    visitor.units[chosen_unit_index].attrib["HP"] += 20
                    visitor.units[chosen_unit_index].attrib["HP"] = min(player.units[chosen_unit_index].attrib["HP"], 100)
                    visitor.coins -= 100
                    valid = True
                else:
                    print(f"\n[-] ERROR. Please choose a valid unit in the range 1-{len(player.units)}\n")
                    if not chosen_unit:
                        print("[-] ERROR. No input provided. Please enter a valid unit number.\n")
            print("\nYou bought a Health Potion. All Player units' HP increased by 20.")
        elif visitor == ai:
            choice = int(random.randint(1, len(ai.units)))
            visitor.units[choice - 1].attrib["HP"] += 20
            visitor.units[choice - 1].attrib["HP"] = min(ai.units[choice - 1]   .attrib["HP"], 100)
            ai.coins -= 100
            print(f"AI chose to increase HP of unit {choice} by 20")
        else:
            print("\nInsufficient Pycoins.")
    elif choice == "2":
        if visitor.coins >= 50 and visitor == player:
            valid = False
            while valid == False:
                chosen_unit = input(f"Which unit do you want to use the Attack Boost on [1-{len(player.units)}]: ")
                if chosen_unit.isdigit() and 1 <= int(chosen_unit) <= len(player.units):
                    chosen_unit_index = int(chosen_unit) - 1
                    visitor.units[chosen_unit_index].attrib["ATK"] += 2
                    visitor.coins -= 50
                    # visitor.units[chosen_unit_index].attrib["ATK"] = min(player.units[chosen_unit_index].attrib["ATK"], 100)
                    valid = True
                else:
                    print(f"\n[-] ERROR. Please choose a valid unit in the range 1-{len(player.units)}\n")
                    if not chosen_unit:
                        print("[-] ERROR. No input provided. Please enter a valid unit number.\n")
            print(f"\nYou bought an Attack Boost. Attack Points of Player Unit {chosen_unit} has been upgraded by 2")
        elif visitor == ai:
            choice = int(random.randint(1, len(ai.units)))
            visitor.units[choice - 1].attrib["ATK"] += 2
            visitor.coins -= 50
            print(f"AI chose to increase Attack of unit {choice} by 2")
        else:
            print("\nInsufficient Pycoins.")
    
    # elif choice == "2":
    #     if visitor.coins >= 50:
    #         visitor.coins -= 50
    #         for unit in visitor.units:
    #             unit.attrib["ATK"] += 2
    #         if visitor == player:
    #             print("\nYou bought an Attack Boost. All Player units' ATK increased by 2.")
    #         else:
    #             print("\nAI bought an Attack Boost from the Pystore. All AI units' ATK increased by 2.")
    #     else:
    #         print("\nInsufficient Pycoins.")
    # elif choice == "3":
    #     if visitor.coins >= 50:
    #         visitor.coins -= 50
    #         for unit in visitor.units:
    #             unit.attrib["DEF"] += 2
    #         if visitor in player.units:
    #             print("\nYou bought a Defense Boost. All PLayer units' DEF increased by 2.")
    #         else:
    #             print("\nAI bought a Defense Boost from the Pystore. All AI units' DEF increased by 2.")
    elif choice == "3":
        if visitor.coins >= 50 and visitor == player:
            valid = False
            while valid == False:
                chosen_unit = input(f"Which unit do you want to use the Defense Boost on [1-{len(player.units)}]: ")
                if chosen_unit.isdigit() and 1 <= int(chosen_unit) <= len(player.units):
                    chosen_unit_index = int(chosen_unit) - 1
                    visitor.units[chosen_unit_index].attrib["DEF"] += 2
                    visitor.coins -= 50
                    # visitor.units[chosen_unit_index].attrib["ATK"] = min(player.units[chosen_unit_index].attrib["ATK"], 100)
                    valid = True
                else:
                    print(f"\n[-] ERROR. Please choose a valid unit in the range 1-{len(player.units)}\n")
                    if not chosen_unit:
                        print("[-] ERROR. No input provided. Please enter a valid unit number.\n")
            print(f"\nYou bought a Defense Boost. Defense Points of Player Unit {chosen_unit} has been upgraded by 2")
        elif visitor == ai:
            choice = int(random.randint(1, len(ai.units)))
            visitor.units[choice - 1].attrib["DEF"] += 2
            visitor.coins -= 50
            print(f"AI chose to increase Defense of unit {choice} by 2")
        else:
            print("\nInsufficient Pycoins.")
        # else:
        #     print("\nInsufficient Pycoins.")
    elif choice == "4":
        print("\nExiting store...\n")
        return
    else:
        print("\nInvalid choice.")
    if visitor == player:
        print(f"\nYou have {visitor.coins} Pycoins remaining\n")
    else:
        print(f"\nAI has {ai.coins} Pycoins remaining\n")


# progress bar elements for HP and others    
def progress_bar(value, field):
    zero = f'''▒▒▒▒▒▒▒▒▒▒ {value} {field}'''
    onetoten = f'''█▒▒▒▒▒▒▒▒▒ {value} {field}'''
    tentotwenty = f'''██▒▒▒▒▒▒▒▒ {value} {field}'''
    twentytothirty = f'''███▒▒▒▒▒▒▒ {value} {field}'''
    thirtytoforty = f'''████▒▒▒▒▒▒ {value} {field}'''
    fortytofifty = f'''█████▒▒▒▒▒ {value} {field}'''
    fiftytosixty = f'''██████▒▒▒▒ {value} {field}'''
    sixtytoseventy = f'''███████▒▒▒ {value} {field}'''
    seventytoeighty = f'''████████▒▒ {value} {field}'''
    eightytoninety = f'''█████████▒ {value} {field}'''
    ninetytohundred = f'''██████████ {value} {field}'''
    
    zeroc = f'''▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ {value} {field}'''
    onetotenc = f'''█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ {value} {field}'''
    tentotwentyc = f'''██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ {value} {field}'''
    twentytothirtyc = f'''███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ {value} {field}'''
    thirtytofortyc = f'''████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ {value} {field}'''
    fortytofiftyc = f'''█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ {value} {field}'''
    fiftytosixtyc = f'''██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ {value} {field}'''
    sixtytoseventyc = f'''███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ {value} {field}'''
    seventytoeightyc = f'''████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒ {value} {field}'''
    eightytoninetyc = f'''█████████▒▒▒▒▒▒▒▒▒▒▒▒▒ {value} {field}'''
    ninetytohundredc = f'''██████████▒▒▒▒▒▒▒▒▒▒▒▒ {value} {field}'''
    hundredtohuntenc = f'''███████████▒▒▒▒▒▒▒▒▒▒▒ {value} {field}'''
    huntentohuntwenc = f'''████████████▒▒▒▒▒▒▒▒▒▒ {value} {field}'''
    huntwentohunthirc = f'''█████████████▒▒▒▒▒▒▒▒▒ {value} {field}'''
    hunthirtohunfortc = f'''██████████████▒▒▒▒▒▒▒▒ {value} {field}'''
    hunforttohunfiftc = f'''███████████████▒▒▒▒▒▒▒ {value} {field}'''
    hunfifttohunsixc = f'''████████████████▒▒▒▒▒▒ {value} {field}'''
    hunsixtohunsevenc = f'''█████████████████▒▒▒▒▒ {value} {field}'''
    hunseventohuneightc = f'''██████████████████▒▒▒▒ {value} {field}'''
    huneighttohunninec = f'''███████████████████▒▒▒ {value} {field}'''
    hunninetotwohundredc = f'''████████████████████ {value} {field}'''
    if field == 'HP':
        if value == 0:
            return zero
        elif value > 0 and value <= 10:
            return onetoten
        elif value > 10 and value <= 20:
            return tentotwenty
        elif value > 20 and value <= 30:
            return twentytothirty
        elif value > 30 and value <= 40:
            return thirtytoforty
        elif value > 40 and value <= 50:
            return fortytofifty
        elif value > 50 and value <= 60:
            return fiftytosixty
        elif value > 60 and value <= 70:
            return sixtytoseventy
        elif value > 70 and value <= 80:
            return seventytoeighty
        elif value > 80 and value <= 95:
            return eightytoninety
        elif value > 95 and value <= 100:
            return ninetytohundred
        else:
            return "Invalid Value"
    elif field == 'Pycoins' or 'Team Strength':
        if value == 0:
            return zeroc
        elif value > 0 and value <= 10:
            return onetotenc
        elif value > 10 and value <= 20:
            return tentotwentyc
        elif value > 20 and value <= 30:
            return twentytothirtyc
        elif value > 30 and value <= 40:
            return thirtytofortyc
        elif value > 40 and value <= 50:
            return fortytofiftyc
        elif value > 50 and value <= 60:
            return fiftytosixtyc
        elif value > 60 and value <= 70:
            return sixtytoseventyc
        elif value > 70 and value <= 80:
            return seventytoeightyc
        elif value > 80 and value <= 95:
            return eightytoninetyc
        elif value > 95 and value <= 100:
            return ninetytohundredc
        elif value > 100 and value <= 110:
            return hundredtohuntenc
        elif value > 110 and value <= 120:
            return huntentohuntwenc
        elif value > 120 and value <= 130:
            return huntwentohunthirc
        elif value > 130 and value <= 140:
            return hunthirtohunfortc
        elif value > 140 and value <= 150:
            return hunforttohunfiftc
        elif value > 150 and value <= 160:
            return hunfifttohunsixc
        elif value > 160 and value <= 170:
            return hunsixtohunsevenc
        elif value > 170 and value <= 180:
            return hunseventohuneightc
        elif value > 180 and value <= 195:
            return huneighttohunninec
        elif value > 195 and value <= 200:
            return hunninetotwohundredc
        else:
            return value, field 

# game introduction
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
    log(banner_text, out)
    print("Welcome to Python Warfare : Terminal Grounds Turn-Based Battle game!")
    log("Welcome to Python Warfare : Terminal Grounds Turn-Based Battle game!", out)
    global player_name
    name_check = True
    while name_check:
        player_name = input("What is your name? ")
        log("What is your name?", out)
        if player_name == "":
            print("[-] ERROR. Please specify a name. You cannot leave this field blank")
            name_check = True
        else:
            print(f"\nHello {player_name}\n")
            name_check = False
        log(player_name, inp)
        log(f"\nHello {player_name}\n", out)
        
    print(f"Okay! let's play, {player_name}! This game allows you to setup a team which is made up of 3 units. The characters available to fill up your 3 units can ONLY be either a (W)arrior or a (T)anker.")
    print(f"Each unit has a:\n(1) Name\n(2) Health Point (HP)\n(3) Attack Point (ATK)\n(4) Defence Point (DEF)\n(5) Experience (EXP)\n(6) Rank: {RANK[0]} | {RANK[1]} | {RANK[2]} | {RANK[3]}")
    log(f"Okay! let's play, {player_name}! This game allows you to setup a team which is made up of 3 units. The characters available to fill up your 3 units can ONLY be either a (W)arrior or a (T)anker.", out)
    log(f"Each unit has a:\n(1) Name\n(2) Health Point (HP)\n(3) Attack Point (ATK)\n(4) Defence Point (DEF)\n(5) Experience (EXP)\n(6) Rank: {RANK[0]} | {RANK[1]} | {RANK[2]} | {RANK[3]}", out)
    cont = input("\nEnter I for instructions or Press return (enter) to continue: ")
    if cont.upper() == "I":
       print('''
===== Game Help =====             

Instructions:

1. The game follows a turn-based battle system.
2. Each player takes turns attacking.
3. On your turn, you will be prompted to select one of your units to attack with.
4. After choosing your attacking unit, you will then select the AI's unit to attack.
5. Damage dealt during the attack is calculated based on the attacker's attack points and the target's defense points.
6. The game continues until all units from one side are defeated.
7. Pay attention to your unit's health and strategize your attacks to defeat the AI's units efficiently.
8. Utilize your units' unique abilities and strengths to gain an advantage in battle.
9. Throughout the game, you can collect Pycoins.
10. Pycoins can be used at the Pystore to purchase power-ups and enhancements for your units.
11. Use your Pycoins wisely to improve your units' abilities and increase your chances of victory.
12. When your unit ranks up, you have the choice to increase either its attack (ATK) or defense (DEF) points by 1.
13. Consider your unit's role and playstyle when deciding to boost ATK or DEF.
14. Manage your resources effectively and make strategic decisions during the game.
15. Remember, in Novice Mode, Pybot will assist you by suggesting unit and target choices. 
16. In Intermediate Mode and Pro Mode, you're on your own. 
17. In Pro Mode, the AI will strategically choose its units to target.
16. All the best and have fun!
''')


        # logging
                    # log("Instructions:", out)
                    # log("1. Each player takes turns attacking.", out)
                    # log("2. You will be prompted to select one of your units to attack with, and then choose the AI's unit to attack.", out)
                    # log("3. Damage dealt is calculated based on the attacker's attack points and the defender's defense points.", out)
                    # log("4. The game continues until all units from one side are defeated.", out)
                    # log("5. Good luck and have fun!\n", out)
    else:
        pass
    global mode
    mode_check = True
    while mode_check:
        try:
            mode = input("Please select your preferred mode of play: (N)ovice, (I)ntermediate, or (P)ro. Enter H to bring up the help menu. ")
            log("Please select your preferred mode of play: (N)ovice, (I)ntermediate, or (P)ro. Enter H to bring up the help menu ", out)
            
            if mode[0].upper() == 'N':
                mode_check = False
                log(mode, inp)
                print("You have chosen to play with a Novice AI. Pybot will assist you throughout the game.")
            elif mode[0].upper() == 'P':
                mode_check = False
                log(mode, inp)
                print("You have chosen to play with a Pro AI")
            elif mode[0].upper() == 'I':
                mode_check = False
                log(mode, inp)
                print("You have chosen to play with an Intermediate AI")
            elif mode[0].upper() == 'H':
                print('''
===== Game Help =====

Choose one of the following game modes:

1. (N)ovice Mode:
- In this mode, the AI will randomly attack your units.
- Pybot will provide assistance by suggesting which unit to send for attack and which AI unit to target.

2. (I)ntermediate Mode:
- This mode is similar to Novice Mode, but without assistance from Pybot.
- The AI will still randomly attack your units.

3. (P)ro Mode:
- In Pro Mode, the AI will strategically choose the unit to attack based on their ATK, DEF, and HP.
- Pybot will not provide any assistance in this mode.
- Be prepared for a challenging gameplay experience!

To select a mode, enter the first letter of the corresponding mode and press Enter.

Have fun and all the best!''')
                mode_check = True
            else:
                print("[-] ERROR. Invalid Input. Please enter N, I, or P to continue")
                mode_check = True
        except IndexError:
            print("[-] ERROR. No value specified. Please enter N, I, or P to continue")





if __name__ == "__main__":
    main()
