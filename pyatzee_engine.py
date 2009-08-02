import scores
from hand import hand

class engine(object):
    
    def __init__(self, view):
        self.view = view
        self.scengine = scores.scoreengine()
        self.start_game()
        
    def start_game(self):
        #start playing yatzee!
        self.h = hand()
        for i in range(0,13):
            self.view.show_scoreboard(self.scengine)
            self.view.show_hand(self.h)
            self.view.get_input(self.h)
            self.h.roll()
            self.view.show_hand(self.h)
            self.view.get_input(self.h)
            self.h.roll()
            self.view.show_hand(self.h)
            self.h.roll()
            self.view.show_potential_points(self.h, self.scengine)
            self.h.unhold_all()
            self.h.roll()
        self.view.show_scoreboard(self.scengine)
            
            
        