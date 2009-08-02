class scoreengine(object):

	def get_possible(self, hand):
		possible_scores = []
		#Ones
		possible_scores.append(score("Ones",self.check_num(1,hand)))
		#Twos
		possible_scores.append(score("Twos",self.check_num(2,hand)))
		#Threes
		possible_scores.append(score("Threes",self.check_num(3,hand)))
		#Fours
		possible_scores.append(score("Fours",self.check_num(4,hand)))
		#Fives
		possible_scores.append(score("Fives",self.check_num(5,hand)))
		#Sixes
		possible_scores.append(score("Sixes",self.check_num(6,hand)))
		#Three of a kind
		possible_scores.append(score("Three of a kind",self.check_of_a_kind(3,hand)))
		#Four of a kind
		possible_scores.append(score("Three of a kind",self.check_of_a_kind(4,hand)))
		#Full House
		#Small Straight
		#Large Straight
		#Chance
		possible_scores.append(score("Chance",sum([x.value for x in hand.dice])))
		#Yatzee
		return filter(lambda x: x.score != 0,possible_scores)
	
	def check_num(self,n,hand):
		counter = 0
		for d in hand.dice:
			if d.value == n: counter += n
		return counter
	
	def check_of_a_kind(self,n,hand):
		vals = []
		for d in hand.dice:
			vals.append(d.value)
		for i in range(1,6):
			if vals.count(i) >= n:
				return sum(vals)
		return 0
				
		
	
class score(object):
	
	def __init__(self, title, score):
		self.title = title
		self.score = score
