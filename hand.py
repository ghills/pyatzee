from dice import dice

class hand(object):
	dice = []
	def __init__(self):
		for i in range(0,5):
			self.dice.append(dice(6))
		for d in self.dice:
			d.roll()
