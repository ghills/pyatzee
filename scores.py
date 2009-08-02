class scoreengine(object):
	score_types = []

	def __init__(self):
		self.populate_scores()

	def get_possible(self, hand):
		return score_types
	
	def populate_scores(self):
		#populate the possible score types
		score_types.append(score("ones",1,1))
	
class score(object):
	
	def __init__(self, title, score, check_function):
		self.title = title
		self.score = score
		self.check_function = check_function
