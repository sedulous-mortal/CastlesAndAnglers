from UserStuff.UserInventory import UserInventory
from Activities.Fishing.FishingActivities import FishingActivities
import Activities.Fishing.Fishes #makes the list of fish available

class User():
	def __init__(self):
		self.name = 'New User'
		self.level = 1
		self.maxHealth = 10 * self.level
		self.healthPoints = self.maxHealth - 1
		self.userInventory = UserInventory()
		self.destinationList = ["the river", "home", "the castle", "the market",
		"the woods"]

	def showHealth(self):
		print(str(self.healthPoints))

	def healUp(self, amount):
		if (self.healthPoints < self.maxHealth):
			self.healthPoints = self.healthPoints + amount
			print('You went up to ' + str(self.healthPoints) + ' hp')
		elif (self.healthPoints > self.maxHealth):
			self.healthPoints = self.maxHealth
			print('You have been restored to max health')
		else:
			print('You are at full health already.')

	def takeDamage(self, amount):
		if (self.healthPoints > 0):
			self.healthPoints = self.healthPoints - amount
		elif (self.healthPoints == 0):
			print('You are already dead and can take no more damage')

	def checkInventory(self):
		print('Inventory contains: ' + str(self.userInventory.listItems()))

	def goFishing(self):
		FishingActivities.goFishing(self)

	def addToInventory(self, item):
		self.userInventory.inventory.append(item)
		print(str(item) + ' added to inventory.')

# Eat Fish function - asks the user which fish they want to eat.
# If the fish is in their inventory and it is a valid name of
# a fish, the fish will be removed from their inventory and
# HP will increase by 1. - Josh 3/24/19
	def eatFish(self):
		fish = input("Which fish would you like to eat?")
		if fish in self.userInventory.inventory:
			if fish in Activities.Fishing.Fishes.Fishes:
				self.userInventory.inventory.remove(fish)
				self.healUp(1)
			else:
				print("Sorry, that's not a fish!")
		else:
			print("Sorry, you don't have that fish!")

	def listDestinations(self):
		print("pick a location to go to:")
		print(self.destinationList)

	def showHelpMenu(self):
		print("Here's what you can do:")
		print("show health")
		print("heal up")
		print("go fishing")
		print("eat a fish")
		print("travel away")
		print("show inventory")
		print("quit")
