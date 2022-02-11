# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Kinnick Fox
# Creation Date: 2/11/2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time


def displayIntro():																	#print() formatting error fixed
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly								
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
																					#removed unneeded print function


def chooseCave():
    cave = ''
																					#removed unneeded while statement
    print('Which cave will you go into? (1 or 2)')
    cave = input()
    return cave																		#corrected return variable name


def checkCave(chosenCave):
    print('You approach the cave...')
    # sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    # sleep for 2 seconds
    time.sleep(3)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
																					#removed unneeded print function
    # sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')										#added parentheses


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':										#changed '=' to boolean '=='
    displayIntro()
    caveNumber = chooseCave()														#function name corrected
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
    if playAgain == "no" or playAgain == 'n':										#added "or playAgain == 'n'" to be consistant with line 48
        print("Thanks for playing")													#grammer corrected
