#!usr/bin/evn Python 

#This is a simple drinking a game each player selects a number and recieves drinking instruction 


number = int(input('Enter between 1 and 10: '))
#if number is out of scope 1-10 print take 5 shots
if number < 1 or number > 10:
    print('Take 5 shots... Got em!')
