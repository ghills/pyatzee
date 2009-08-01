import random

class dice(object):
	held = False

	def __init__(self, sides):
		random.seed()
		self.sides = sides
		self.value = sides

	def roll(self):
		self.value = random.randint(1,6)

	def __str__(self):
		return str(self.value)
