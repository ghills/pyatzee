#!/usr/bin/python

from dice import dice
from hand import hand
from scores import scoreengine

h = hand()
hand.dice[0].held = True
print [d.value for d in hand.dice]
print [d.held for d in hand.dice]

se = scoreengine()
print ["%s: %d" % (s.title, s.score(h)) for s in se.get_possible(h)]