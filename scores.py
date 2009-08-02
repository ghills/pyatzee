class scoreengine(object):
	score_types = []
	
	def __init__(self):
		self.populate_types()
	
	def get_possible(self, hand):
		return filter(lambda x: not x.used,self.score_types)
	
	def populate_types(self):
		self.score_types.append(score("Ones",lambda x: [d.value for d in x.dice].count(1)))
		self.score_types.append(score("Twos",lambda x: 2 * [d.value for d in x.dice].count(2)))
		self.score_types.append(score("Threes",lambda x: 3 * [d.value for d in x.dice].count(3)))
		self.score_types.append(score("Fours",lambda x: 4 * [d.value for d in x.dice].count(4)))
		self.score_types.append(score("Fives",lambda x: 5 * [d.value for d in x.dice].count(5)))
		self.score_types.append(score("Sixes",lambda x: 6 * [d.value for d in x.dice].count(6)))
		self.score_types.append(score("Three of a kind",self.three_of_kind))
		self.score_types.append(score("Four of a kind",self.four_of_kind))
		self.score_types.append(score("Full House",self.full_house))
		self.score_types.append(score("Small Straight",self.small_straight))
		self.score_types.append(score("Large Straight",self.large_straight))
		self.score_types.append(score("Yatzee",self.yatzee))
		self.score_types.append(score("Chance",lambda x: sum([d.value for d in x.dice])))
	
	def get_scoreboard(self):
		result = []
		for type in self.score_types:
			if type.used: result.append([type.title, str(st.calcscore)])
			else: result.append([type.title,"-"])
		return result
	
	def three_of_kind(self,hand):
		vals = [d.value for d in hand.dice]
		if max([vals.count(i) for i in range(1,7)]) >= 3: return sum(vals)
		else: return 0
	
	def four_of_kind(self,hand):
		vals = [d.value for d in hand.dice]
		if max([vals.count(i) for i in range(1,7)]) >= 4: return sum(vals)
		else: return 0
	
	def full_house(self,hand):
		vals = [d.value for d in hand.dice]
		countvals = [vals.count(i) for i in range(1,7)]
		if countvals.count(3) == 1 and countvals.count(2) == 1: return 25
		else: return 0
		
	def small_straight(self,hand):
		countvals = map(self.hasit,[[d.value for d in hand.dice].count(i) for i in range(1,7)])
		strvals = "".join(map(str,countvals))
		if strvals.find("1111") >= 0: return 30
		else: return 0
		
	def large_straight(self,hand):
		countvals = map(self.hasit,[[d.value for d in hand.dice].count(i) for i in range(1,7)])
		strvals = "".join(map(str,countvals))
		if strvals.find("11111") >= 0: return 40
		else: return 0
	
	def hasit(self,x):
		if x>0: return 1
		else: return 0
	
	def yatzee(self,hand):
		vals = [d.value for d in hand.dice]
		countvals = [vals.count(i) for i in range(1,7)]
		if countvals.count(5) == 1: return 50
		else: return 0

	
class score(object):
	calcscore = 0
	used = False
	def __init__(self, title, score):
		self.title = title
		self.score = score
	def use(self,hand):
		points = self.score(hand)
		self.score = lambda x: points
		calcscore = int(points)
		
