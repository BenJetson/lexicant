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

def add_letter(text):
    if "+" in text and len(text) == 2 and text!= "++":
        if text.endswith("+"):
            text = text.strip("+") + text
        elif text.startswith("+"):
            text += text.strip("+")

def is_whole_word(text):
    if text in word_list:
        return True
    
    return False

def is_partial_word(text):
    for i in word_list:
        if text in i:
            return True
    
    return False
   
def play(players, word_list):
    pass

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
