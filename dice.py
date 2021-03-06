import random
"""
Dice class, represents a die in a game.
Pass it an integer for the number of sides it should have.
"""
class dice(object):
	held = False

	def __init__(self, sides):
		random.seed()
		self.sides = sides
		self.value = sides

	def roll(self):
		self.value = random.randint(1,self.sides)

	def __str__(self):
		return str(self.value)
