# Computer Programming 1
# Lexicant
#
# Name: 
# Date: 

#global config
word_list_path = "freebsd2.txt"


def load_word_list(path):
    pass

def show_start_screen():
    pass

def show_credits():
    pass

def show_menu():
    pass

def show_rules():
    pass

def get_player_names():
    pass

def add_letter(text):
    pass

def is_whole_word(text):
    pass

def is_partial_word(text):
    pass
   
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
