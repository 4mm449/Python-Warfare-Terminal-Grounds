import character
player_units = []
ai_units = []
# game_over = False
UNIT = 3
RANK = ["Bronze", "Silver", "Gold", "Diamond"]
# main function
def main():
    game_intro()
    unit = 0
    # prompt user for player unit details
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
                    # player_units = character.Player.add_unit(temp_player_units)
                    player_units.append(str(temp_player_units))
                    print(player_units)
                    profession_check = False
                else:
                 profession = input(f"[-] ERROR, BAD INPUT. Enter W for Warrior or T for Tanker for Unit {i + 1}: ")
            except:
                profession = input("[-] ERROR. No value specified. Please specify a value [W/T]: ")
    game =  character.Character(name, profession, unit)
    game.game()
    
  


                 
                 

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
