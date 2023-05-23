import character
import random
player_units = []
ai_units = []
game_over = False
rounds = 1
UNIT = 3
RANK = ["Bronze", "Silver", "Gold", "Diamond"]
# main function
def main():
    game_intro()
    unit = 0
    
    # prompt user for player unit details, setup player units
    for i in range(UNIT):
        name = input(f"(1) Enter the name for Unit {i + 1}: ")
        profession = input(f"(2) Choose either (W)arrior or (T)anker for Unit {i + 1}: ")
        profession_check = True
        unit += 1
        while profession_check:
            try:
                if profession[0].upper() == 'W' or profession[0].upper() == 'T':
                    profession = profession[0].upper()
                    temp_player_units = str(character.Character(name, profession, unit))
                    print(temp_player_units)
                    # player_units = character.Player.add_unit(temp_player_units)
                    player_units.append(temp_player_units)
                    print(player_units)
                    profession_check = False
                else:
                 profession = input(f"[-] ERROR, BAD INPUT. Enter W for Warrior or T for Tanker for Unit {i + 1}: ")
            except:
                profession = input("[-] ERROR. No value specified. Please specify a value [W/T]: ")
   
    player_unit1 = player_units[0]
    player_unit2 = player_units[1]
    player_unit3 = player_units[2]
    
    # unit = 0
    # setup AI units
    choice = ["W", "T"]
    for i in range(UNIT):
        aname = f"AI{random.randint(1, 99)}"
        aprofession = random.choice(choice)
        temp_ai_units = str(character.Character(aname, aprofession, unit))
        ai_units.append(temp_ai_units)
        
    ai_unit1 = ai_units[0]
    ai_unit2 = ai_units[1]
    ai_unit3 = ai_units[2]
        
    game =  character.Character(name, profession, unit)
    try_again = True
    while game_over == False:
        while try_again:
            if rounds % 2 == 1:
                print(f"It's {player_name}'s turn to attack")
                display_stats = True
                while display_stats:
                    attacker = input("Enter unit that you wish to send for an attack [1-3] or type U to check unit stats: ")
                    try:
                        if attacker == "U":
                            # display_gamestats()
                            print(player_units)
                            print(ai_units)
                            display_stats = False
                            attacker = input("Enter unit that you wish to send for an attack [1-3]: ")
                            victim = input("Enter AI unit that you wish to attack [1-3]: ")
                        else:
                            victim = input("Enter AI unit that you wish to attack [1-3]: ")
                    except:
                        attacker = input("[-] ERROR. No value specified. Please specify a value [1-3 or U]: ")
                    
                    #AI chooses attack

                    victim = random.choice(player_units)
                    attacker = random.choice(ai_units)   
                    
  


                 
                 
# print(game stats)
def display_gamestats():
    # player_units = [player_unit1, player_unit2, player_unit3]
    # ai_units = [ai_unit1, ai_unit2, ai_unit3]
    # print("---------------------------\n")

    # print("---------------------------")
    # print("Player Unit {}:            |\n---------------------------\n(1) Name: {Name}\n(2) Profession: {Profession}\n(3) Health Point (HP): {HP}\n(4) Attack Point (ATK): {ATK}\n(5) Defence Point (DEF): {DEF}\n(6) Experience (EXP): {EXP}\n(7) Rank: {Rank}" .format(i + 1, **player_unit))
    # print("---------------------------\n")
    # print(f"AI TEAM:\n\nAI Unit 1: {ai_unit1}\nAI Unit 2: {ai_unit2}\nAI Unit 3: {ai_unit3}\n")
    #display player stats
    print("---------------------------")
    print("Player Unit 1:             |\n---------------------------\n(1) Name: {Name}\n(2) Profession: {Profession}\n(3) Health Point (HP): {HP}\n(4) Attack Point (ATK): {ATK}\n(5) Defence Point (DEF): {DEF}\n(6) Experience (EXP): {EXP}\n(7) Rank: {Rank}" .format(i + 1, **player_unit1))
    print("---------------------------\n")

    print("---------------------------")
    print("Player Unit 2:             |\n---------------------------\n(1) Name: {Name}\n(2) Profession: {Profession}\n(3) Health Point (HP): {HP}\n(4) Attack Point (ATK): {ATK}\n(5) Defence Point (DEF): {DEF}\n(6) Experience (EXP): {EXP}\n(7) Rank: {Rank}" .format(i + 1, **player_unit2))
    print("---------------------------\n")

    print("---------------------------")
    print("Player Unit 3:             |\n---------------------------\n(1) Name: {Name}\n(2) Profession: {Profession}\n(3) Health Point (HP): {HP}\n(4) Attack Point (ATK): {ATK}\n(5) Defence Point (DEF): {DEF}\n(6) Experience (EXP): {EXP}\n(7) Rank: {Rank}" .format(i + 1, **player_unit3))
    print("---------------------------\n")


    print("***************************\n")

    #display ai stats
    print("---------------------------")
    print("AI Unit 1:                 |\n---------------------------\n(1) Name: {Name}\n(2) Profession: {Profession}\n(3) Health Point (HP): {HP}\n(4) Attack Point (ATK): {ATK}\n(5) Defence Point (DEF): {DEF}\n(6) Experience (EXP): {EXP}\n(7) Rank: {Rank}" .format(i + 1, **ai_unit1))
    print("---------------------------\n")

    print("---------------------------")
    print("AI Unit 2:                 |\n---------------------------\n(1) Name: {Name}\n(2) Profession: {Profession}\n(3) Health Point (HP): {HP}\n(4) Attack Point (ATK): {ATK}\n(5) Defence Point (DEF): {DEF}\n(6) Experience (EXP): {EXP}\n(7) Rank: {Rank}" .format(i + 1, **ai_unit2))
    print("---------------------------\n")

    print("---------------------------")
    print("AI Unit 3:                 |\n---------------------------\n(1) Name: {Name}\n(2) Profession: {Profession}\n(3) Health Point (HP): {HP}\n(4) Attack Point (ATK): {ATK}\n(5) Defence Point (DEF): {DEF}\n(6) Experience (EXP): {EXP}\n(7) Rank: {Rank}" .format(i + 1, **ai_unit3))
    print("---------------------------\n")

def game_intro():
    banner_text = '''                                            
 _____     _   _   _        _____             _     
| __  |___| |_| |_| |___   | __  |___ _ _ ___| |___ 
| __ -| .'|  _|  _| | -_|  |    -| . | | | .'| | -_|
|_____|__,|_| |_| |_|___|  |__|__|___|_  |__,|_|___|
                                     |___|          
    '''
                                                        

    print(banner_text)
    print("Welcome to this Turn-Based Battle game!")
    global player_name
    player_name = input("What is your name? ")
    print(f"\nHello {player_name}\n")
    init1 = print(f"Okay! let's play, {player_name}! This game allows you to setup a team which is made up of 3 units. The characters available to fill up your 3 units can ONLY be either a (W)arrior or a (T)anker.")
    init2 = print(f"Each unit has a:\n(1) Name\n(2) Health Point (HP)\n(3) Attack Point (ATK)\n(4) Defence Point (DEF)\n(5) Experience (EXP)\n(6) Rank {RANK}")
    input("\nPress return to continue...")
    # logfile.write(banner_text + "\n")
    # logfile.write("What is your name? " + "\n")
    # logfile.write(player_name + "\n") 
    
main()
