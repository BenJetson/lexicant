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
    print("Type 1 to begin playing!")
    print("Type 2 to view the rules.")
    print("Type 3 to exit.")
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

def get_start_letter():
    while True:
        print("Please input a starting letter.")
        text = input("> ")
        
        if len(text) == 1 and text.islower() and text.isalpha():
            return text

            
def play(players, word_list):
    whole_word = False
    partial_word = True
    num_players = len(players)
    turn = num_players + 1 
    # The initial value is set to this so it will get
    # set to 0 when the game loop starts.
    
    text = get_start_letter()
    
    while not whole_word and partial_word:
        
        turn = (turn + 1) % num_players
        
        print("--Player", players[turn], "is up!--")
        
        while True:
            print()
            print("Enter a letter preceded or followed by a + sign.")
            letter = input("> ")
            
            if "+" in letter and len(letter) == 2 and letter != "++":
                text = add_letter(letter, text)
                break
            else:
                print("Invalid input. Try again")
            
        partial_word = is_partial_word(text, word_list)
        
        if partial_word and len(text) > 3:
            whole_word = is_whole_word(text, word_list)
        
        # This will be spruced up later, but for now, it works!
        print("Text:", text)
        print("Partial:", partial_word, "Whole:", whole_word)
    
    
    # Game over screen. Probably will be moved to a function later.
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
    loser = "Player " + players[turn] + " loses!"
    print(loser.center(62, " "))
        
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
