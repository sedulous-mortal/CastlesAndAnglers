import random
from .FishHelperFunctions import *
from .Fishes import Fishes

class FishingActivities():

	def castPole():
		chars = [',', '.', ':', '\'']
		chars2 = [] + chars
		chars2.reverse()
		totalChars = chars + chars2
		for char in totalChars:
			for i in range(0, 3):
				specialPrint(char)
				rapidTween()
				i += i
		print()

	@classmethod
	# cls is used to show I'm calling the methods
	# inside of the class instead of 
	# referring to self
	def goFishing(cls, user):
		outcomes = ['win', 'lose', 'draw']
		print('You are fishing\n')
		cls.castPole()
		random.shuffle(outcomes)
		currentFishingOutcome = outcomes[0]
		if (currentFishingOutcome == 'win'):
			user.addToInventory(cls.catchFish())
		if (currentFishingOutcome == 'lose'):
			print('you did not catch a fish this time')
		if (currentFishingOutcome == 'draw'):
			print('you caught a lure')
			user.addToInventory('lure')

	def catchFish():
		random.shuffle(Fishes)
		randomFish = Fishes[0]
		print('you caught a ' + randomFish)
		return randomFish