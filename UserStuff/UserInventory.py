class UserInventory():

	def __init__(self):
			self.inventory = []
			self.startingInventory = ['fishing rod', 'bread', 'bow', 'arrows']
			self.x = 0
			self.y = 0
			self.populate()

	def listItems(self):
			return self.inventory

	def populate(self):
		self.inventory = []
		for item in self.startingInventory:
			self.inventory.append(item)
