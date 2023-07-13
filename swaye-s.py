#!usr/bin/python3
"""The game is a drinking game meant to be played with 4 or more people randomized name selection and drink commands"""
import random
import loader
# List of all the players names 
player_list=[]
# List of all the drinking commands 
instruction_list=['take 1 shot',
                 'take 2 shots',
                 'phone a friend to take 2 shots with you',
                 'take a shot off someone\, of the most sober player\'s choosing',
                 'take 3 shots or do a dance\, *twerking counts*',
                 'divy up 5 shots amoung friends',
                 'stand on 1 leg and rub your head while taking 1 shot',
                 'tell everyone one of your secrets they do not know or take 2 1/2 shots',
                 'take 2 shots and give someone else a shot',
                 'sing a song\, choosen by the most inebriated player or everyone takes a shot but you',
                 'pick 3 players and they take 1 shot each',
                 'the previous player chooses to either take a or every other player takes 2 shots',
                 'tell an embarrassing true story or take 2 shots'
                 'choose one other player to sing a song with you\, if the rest of the players like your performance no shot if they don\'t then 1 shot for each of you singing',
                 'What is the most broke thing you\'ve ever done? or take a shot',] 
# Start of menu and first steps 
def menu():
    print("==== Game Start Menu ====")
    print("This is only the Begining")
    print("*************************")
    #Start an infinite loop 

    #Ask user for a selection
    choice =input("would you like to play? (y or n)")

    # check if they entered y or n
    if choice.lower() == 'n':
        print("See You Soon!")
        
    elif choice.lower() == 'y':
        print('Lets Play a Game!')
 # Collecting players names for player list            
def player():
    while True:
        name =input('Input player name >>> ')
        player_list.append(name)
        followup =input('Add new player? y/n ')
        if followup.lower() == 'n':
            break
        else:
            continue
    print(player_list)
        
 # Game logic here 
def game():
    """ called at run time """
    while True:
        challenge = random.choice(instruction_list)
        player = random.choice(player_list)
        
        with loader("Loading with context manager..."):
            for i in range(10):
                sleep(0.25)
        
        loader = loader("Loading with object...", "That was fast!", 0.05).start()
        for i in range(10):
            sleep(0.25)
            loader.stop()
        print(player)
        print(challenge)
        print('press *c* to continue\, or press *esc*')
        pimp =input() 

        if pimp.lower() == 'c':
            continue 
            

        else:
            break
        
def main():
    # show menu
    menu()
    # add players 
    player()
    # start game loop
    game()
    # while loop 
    # load annimation
    loader()
    # Pick random player


if __name__ == "__main__":
    main()

