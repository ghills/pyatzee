#!/usr/bin/python

from dice import dice
from hand import hand

"""
x = dice(6)
print x.value
x.roll()
print x.value
"""

h = hand()
hand.dice[0].held = True
print [d.value for d in hand.dice]
print [d.held for d in hand.dice]

