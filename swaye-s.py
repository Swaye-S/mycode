#!usr/bin/python3
"""The game is a drinking game meant to be played with several people.randomized name selection and drink commands"""
Player list[]
Order list[take 1 shot, ] 
1=='take 1 shot' 
2=='take 2 shots'
3=='take 2 shots and give someone else a shot'
4=='take 3 shots or do a dance'
5=='stand on 1 leg and rub your head while taking 1 shot'
6=='pick someone to take a shot off'
7=='divy up 5 shots amoung friends'
#This is a simple drinking a game each player selects a number and recieves drinking instruction
def menu():
    print("=== Game Start Menu ===")
    print("This is only the Begining")
    print("************************")
    #Start an infinite loop 
    while True:
        #Ask user for a selection
        choice =input("would you like to play? (y or n)")

        # check if they entered y or n
        if choice.lower() == 'n':
            print("See You Soon!")
            break 
        elif choice.lower() == 'y':
            print('Lets Play a Game!')
    def player():
            while True:
                p1 =input('Enter Name For Player 1 ' ) 
                choice =input('Would You Like To Add A Player? (y or n) ')
                if choice.lower() == 'y':
                    p2 =input('Input New Player ')
                elif choice.lower() == 'n':

            # put game logic here 
            break
        else:
            print('Try again')
def main():
    # show menu
    menu()
    # add players 

    # while loop 
    # Pick random player

if __name__ == "__main__":
    main()


number = int(input('Enter between 1 and 10: '))
#if number is out of scope 1-10 print take 5 shots
if number < 1 or number > 10:
    print('Take 5 shots... Got em!')
