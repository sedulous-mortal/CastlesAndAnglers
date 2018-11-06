#import math
#import numpy
#import matplotlib

from GameInstance import GameInstance

# debugging this:
# TypeError: 'module' object is not callable

# proposed solution:
# from YourClassParentDir.YourClass import YourClass

# doesn't work:
# import main

def mainFunc():
	myGame = GameInstance()
	print('Welcome to Crafters Castle!')
	print('To play, please type in an activity, such as "show health" or "session time" \n')
	myGame.startGame()

mainFunc()