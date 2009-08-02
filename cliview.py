from pyatzee_engine import engine

class cliview(object):
    
    def __init__(self):
        print "Welcome to Pyatzee!!\n"
        self.engine = engine(self)
    
    def show_scoreboard(self,scoreengine):
        #show the scoreboard from the engine
        print "scoreboard"
    
    def show_hand(self,hand):
        #show the hand you have, choose what to hold
        print "hand"
        
    def show_potential_points(self, hand, scoreengine):
        #show the potential point breakdown for this hand
        print "potential points"