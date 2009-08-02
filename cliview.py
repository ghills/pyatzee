from pyatzee_engine import engine

import hand
class cliview(object):
    
    def __init__(self):
        print "Welcome to Pyatzee!!\n"
        self.engine = engine(self)
    
    def show_scoreboard(self,scoreengine):
        #show the scoreboard from the engine
        for type in scoreengine.get_scoreboard():
            print "%s: %s" % (type[0],type[1])
    
    def show_hand(self,hand):
        #show the hand you have, choose what to hold
        for i in range(1,6):
            if hand.dice[i-1].held: isheld = "*"
            else: isheld = ""
            print "(%d): %d %s" % (i,hand.dice[i-1].value,isheld)
       
            
    def get_input(self, hand):
        i = raw_input("select holds> ")
        hold_vals = i.split(" ")
        hold_vals = map(int,hold_vals)
        hand.unhold_all()
        for val in hold_vals:
            hand.dice[val - 1].held = True
        
        
    def show_potential_points(self, hand, scoreengine):
        #show the potential point breakdown for this hand
        possibles = scoreengine.get_possible(hand)
        print "Possible point vals:\n-------------"
        pairs = {}
        i = 1
        for st in possibles:
            print "(%d) %s: %d" % (i,st.title,st.score(hand))
            pairs[i] = st
            i += 1
        i = raw_input("select to use> ")
        st = pairs[int(i)]
        st.use(hand)