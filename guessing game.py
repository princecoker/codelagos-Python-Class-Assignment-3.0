#python program to make a guessing game
#import random library
#make a range of values between 1 and 100 where random numbers will be selected
import random
random_number = random.randint(1,100)


#use this to guide how close of far player is from random number
upper_limit = random_number + 10
lower_limit = random_number - 10


#displays answer. Not necessary but helps to test if program runs fine
print (random_number)


#Give instruction, collect player name and request player to type yes to play
print ('''This is a guessing game
1. Type your name to play
2. Type yes to proceed
3. COntinue guessing a number until you get the number selected by computer \n\n''')
       
player_name = str(input('What is your name please?----> '))
print ('Dear',player_name,'if you desire to play this game type "yes"\n')
play = str(input('Do you want to play the random game?----> '))


#Loop starts while play is yes
#it collects guessed number, checks if it is equal to,close to or far off from random number and print desired output
while play == 'yes':
    guess = int(input('What is your guess?\n'))
    if (guess == random_number):
        print(player_name.upper(),'YOU ARE CORRECT\n')
        break
    elif (guess <= upper_limit) and (guess >= lower_limit):
        print (player_name.upper(),'YOU ARE ALMOST THERE\n')
        print ('try again')
    elif (guess < lower_limit) or (guess > upper_limit):
        print (player_name.upper(),'YOU ARE FAR OFF\n')
        print ('try again')
    else:
        print ()


#says goodbye once game is completed.      
print ('Good Bye')

