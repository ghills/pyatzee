from dice import dice

class hand(object):
	dice = []
	def __init__(self):
		for i in range(0,5):
			self.dice.append(dice(6))
		for d in self.dice:
			d.roll()
			
	def unhold_all(self):
		for d in self.dice: d.held = False
	
	def roll(self):
		for d in filter(lambda x: not x.held,self.dice): d.roll()
		
	
