#!usr/bin/env python3
'''Author Kwintin Cox aka Swaye: The game is a simple drinking game.'''
# Imported Modules 
import random
from loaders import SpinningLoader
import crayons
#nfrom colr import color
player_list = []
instruction_list = ['take 1 shot',
                   'take 2 shots',
                   'phone a friend to take 2 shots with you',
                   'take a shot off someone, of the most sober player\'s choosing',
                   'take 3 shots or do a dance.',
                   'divy up 5 shots among friends',
                   'stand on 1 leg and rub your head while taking 1 shot',
                   'tell everyone 1 of your secrets they do not know or take 2 1/2 shots',
                   'take 2 shots and give someone else 1 shot',
                   'sing a song, chosen by the most inebriated player or everyone takes 1 shot but you',
                   'pick 3 players and they take 1 shot each',
                   'the previous player chooses to either take 1 shot or every other player takes 2 shots',
                   'tell an embarrassing true story or take 2 shots',
                   'choose one other player to sing a song with you, if the rest of the players like your performance take no shot if they don\'t then 1 shot for each singer',
                   'What is the most broke thing you\'ve ever done? or take 1 shot',]
# Start of menu display 
def menu():
    print(crayons.green("==== Game Start Menu ===="))
    print(crayons.red("This is only the Beginning"))
    print(crayons.black("**************************"))
# Ask user for a selection
    while True:
        choice = input(crayons.magenta("Would you like to play? (y/n) "))
# Check if they entered y or n
        if choice.lower() == 'n':
            print("See You Soon!")
            exit()
        elif choice.lower() == 'y':
            print(crayons.red('Let\'s Play a Game!'))
            break
        else:
            print(crayons.blue('You can do better than that'))
            continue
# Adding players 
def add_players():
    while True:
        name = input(crayons.blue('Input player name >>> '))
        player_list.append(name)
        follow_up = input(crayons.yellow('Add new player? (y/n) '))
        if follow_up.lower() == 'n':
            break
        elif follow_up.lower() == 'y':
            continue
    print(player_list)
# Game logic
def game():
    """ called at run time """
# Randomize selection of name and drink instructions    
    while True:
        challenge = random.choice(instruction_list)
        random_player = random.choice(player_list)
        fixed_loader = SpinningLoader(text='Players Get Ready To Blackout', style='underline', colour='blue', size='large', speed=.06, duration=20)
        fixed_loader.run() # Pauses program execution and runs loader for 10s
        print(crayons.magenta(random_player))
        fixed_loader.run()
        print(crayons.red(challenge))
        print(crayons.green('Press *c* to continue, or press *esc*'))
        choice = input()
        if choice.lower() == 'c':
            continue
        else:
            break
# Project structor and execution
def main():
    menu()
    add_players()
    game()
if __name__ == "__main__":
    main()
