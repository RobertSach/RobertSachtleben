# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Robert Sachtleben
# Creation Date: 2/14/2023
# Below is a simple program with several.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
  
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()


def chooseCave():
    cave = ''
  # It looks like you had an indent error here
  
       #while cave != '1' and cave != '2':
           # print('Which cave will you go into? (1 or 2)')
            #cave = input()
    while cave != '1' and cave != '2':
            print('Which cave will you go into? (1 or 2)')
            cave = input()
#I believe you meant return cave
    #return caves
    return cave
# It looks like you meant to put "chooseCave" instead of "chosenCave"
#def checkCave(chosenCave):
def checkCave(chooseCave):
    print('You approach the cave...')
    #sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    #sleep for 2 seconds
    time.sleep(3)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    #sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)
    #Again you put chosenCave instead of ChooseCave
    #if chosenCave == str(friendlyCave):
    if chooseCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
      #It looks like you were missing a parentheses 
        #print 'Gobbles you down in one bite!'
      print('Gobbles you down in one bite!')

displayIntro()
#You forgot to capitalize cave in chooseCave
#caveNumber = choosecave()
caveNumber = chooseCave()
checkCave(caveNumber)
 # There is a typo here   
#print("Thanks for planing")
print ("Thanks for playing")