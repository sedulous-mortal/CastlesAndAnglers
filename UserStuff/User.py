from UserStuff.UserInventory import UserInventory
from Activities.Fishing.FishingActivities import FishingActivities

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
			self.healthpoints = self.healthPoints - amount
		elif (self.healthPoints == 0):
			print('You are already dead and can take no more damage')

	def checkInventory(self):
		print('Inventory contains: ' + str(self.userInventory.listItems()))

	def goFishing(self): 
		FishingActivities.goFishing(self)

	def addToInventory(self, item):
		self.userInventory.inventory.append(item)
		print(str(item) + ' added to inventory.')
	
	def listDestinations(self):
		print("pick a location to go to:")
		print(self.destinationList)