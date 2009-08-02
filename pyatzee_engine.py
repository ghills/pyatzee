import scores
from hand import hand

class engine(object):
    
    def __init__(self, view):
        self.view = view
        self.scoreengine = scores.scoreengine()
        self.start_game()
        
    def start_game(self):
        #start playing yatzee!
        self.hand = hand()
        for i in range(0,13):
            self.view.show_scoreboard(self.scoreengine)
            self.view.show_hand(self.hand)
            self.hand.roll()
            self.view.show_hand(self.hand)
            self.hand.roll()
            self.view.show_hand(self.hand)
            self.hand.roll()
            self.view.show_potential_points(self.hand, self.scoreengine)
        self.view.show_scoreboard(self.scoreengine)
            
            
        