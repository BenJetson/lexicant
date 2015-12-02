# Computer Programming 1
# Lexicant
#
# Name: Ben Godfrey
# Date: 11/23/2015

#global config
word_list_path = "./freebsd2.txt"


def load_word_list(path):
    with open(path, 'r') as file:
        dictionary = file.read().splitlines()
    
    return dictionary

def show_start_screen():
    print("""
  _  _  ____  __     ___  __   _  _  ____    ____  __  
 / )( \(  __)(  )   / __)/  \ ( \/ )(  __)  (_  _)/  \  
 \ /\ / ) _) / (_/\( (__(  O )/ \/ \ ) _)     )( (  O ) 
 (_/\_)(____)\____/ \___)\__/ \_)(_/(____)   (__) \__/ 
    __    ____  _  _  __  ___   __   __ _  ____  _     
   (  )  (  __)( \/ )(  )/ __) / _\ (  ( \(_  _)/ \    
   / (_/\ ) _)  )  (  )(( (__ /    \/    /  )(  \_/    
   \____/(____)(_/\_)(__)\___)\_/\_/\_)__) (__) (_)  """)
    print()

def show_credits():
    print("""
 ___                      __      ___  __   __  
  |  |__|  /\  |\ | |__/ /__`    |__  /  \ |__) 
  |  |  | /--\ | \| |  \ .__/    |    \__/ |  \ 
   
        __                       __    /       
       |__) |    /\  \ / | |\ | / _`  /        
       |    |__ /--\  |  | | \| \__| .         """)
    print()
    print("      Program written by Ben Godfrey.")
    print("               11/23/2015")
    print()
    
def show_menu():
    print(" " + ("_" * 54))
    print("/" + (" " * 54) + "\ ")
    print("|" + "--Lexicant Game Menu--".center(54, " ") + "|")
    print("|" + (" " * 54) + "|")
    print("|" + "Choose 1 to begin playing!".center(54, " ") + "|")
    print("|" + "Choose 2 to view the rules.".center(54, " ") + "|")
    print("|" + "Choose 3 to exit.".center(54, " ") + "|")
    print("\______________________________________________________/")
    print()

def show_rules():
    print()
    print("""
---LEXICANT RULES---
Lexicant is a word game played by two people. To start,
a player chooses a letter. The next player adds a letter
to the beginning or the end of the letters to begin 
forming a word. The first player to make a word loses.

If a player adds a letter to make the letters not part
of a word, the other player wins.

When prompted, to add a letter to the beginning of the 
letters, type the letter followed by +. Ex. a+
To add a letter to the end of the word, type a + followed
by the letter. Ex. +e """)
    print()

def get_player_names():
    player1 = input("Enter the name for player 1: ")
    player2 = input("Enter the name for player 2: ")
    
    return [player1, player2]

def add_letter(letter, text):
    
    if letter.endswith("+") and letter[0].isalpha() and letter[0].islower():
        return (letter.strip("+") + text)
    elif letter.startswith("+") and letter[-1].isalpha() and letter[-1].islower():
        return (text + letter.strip("+"))

def is_whole_word(text, word_list):
    if text in word_list:
        return True
    
    return False

def is_partial_word(text, word_list):
    for i in word_list:
        if text in i:
            return True
    
    return False

def get_start_letter(players):
    print("--Player", players[0], "is up!--")
    while True:
        print("Please input a starting letter.")
        text = input("> ")
        
        if len(text) == 1 and text.islower() and text.isalpha():
            print()
            return text
            
        print("Invalid input.")
        print()

def game_over_splash(players, turn, partial_word, whole_word, text):
    print()
    print("""
                   *              )               (      ____ 
 (        (      (  `          ( /(               )\ )  |   / 
 )\ )     )\     )\))(   (     )\()) (   (   (   (()/(  |  /  
(()/(  ((((_)(  ((_)()\  )\   ((_)\  )\  )\  )\   /(_)) | /   
 /(_))_ )\ _ )\ (_()((_)((_)    ((_)((_)((_)((_) (_))   |/    
(_)) __|(_)_\(_)|  \/  || __|  / _ `\ \ / / | __|| _ \ ( )    
  | (_ | / _ \  | |\/| || _|  | (_) |\ V /  | _| |   / )\     
   \___|/_/ \_\ |_|  |_||___|  \___/  \_/   |___||_|_\((_)    """)
    
    print()
    
    if whole_word:
        print(("You lost because " + text + " is a whole word.").center(62, " "))
    else:
        print(("Bluff! " + text + " is not part of any word we know.").center(62, " "))
    
    print()
    print(("Player " + players[turn] + " wins!").center(62, " "))
    print((players[(turn - 1)] + " loses!").center(62, " "))
    
    
def get_letter():
    while True:
        print("Enter a letter preceded or followed by a + sign.")
        letter = input("> ")
        
        if "+" in letter and len(letter) == 2 and letter != "++":
            return letter
        else:
            print("Invalid input. Try again")
                
def play(players, word_list):
    # Sets initial values
    whole_word = False
    partial_word = True
    num_players = len(players)
    turn = 1
    text = get_start_letter(players)
    
    while not whole_word and partial_word:
        
        print(("--Player " + players[turn] + " is up!--").center(51, " "))
        print()
        
        letter = get_letter()
        
        text = add_letter(letter, text)
             
        partial_word = is_partial_word(text, word_list)
        
        if partial_word and len(text) > 3:
            whole_word = is_whole_word(text, word_list)
        
        if not whole_word and partial_word: 
            print("  ___________________________________________________")
            print(" /                                                   \ ")
            print(" |" + ("The word so far: " + text.upper()).center(51, " ") + "|")
            print(" \___________________________________________________/ ")
            print()
        
        turn = (turn + 1) % num_players
    
    game_over_splash(players, turn, partial_word, whole_word, text)
    
        
# main - DO NOT MODIFY CODE BELOW THIS LINE!
show_start_screen()

again = True
    
while again:

    show_menu()
    selection = input("What would you like to do? ")
    
    if selection == "1":
        players = get_player_names()
        word_list = load_word_list(word_list_path)
        play(players, word_list)
        
    elif selection == "2":
        show_rules()
        
    elif selection == "3":
        again = False
        
    else:
        print("Invalid selection.")

    print()

show_credits()
