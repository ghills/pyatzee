import random
import unittest

class TestDiceFunctions(unittest.TestCase):
	def setUp(self):
		self.dice = Dice(6)

	def testroll(self):
		self.dice.roll()
		for i in range(1,100):
			self.assert_(self.dice.value in range(1,6))
	
if __name__ == '__main__':
	unittest.main()
