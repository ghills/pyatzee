#!/usr/bin/python

from dice import dice
from hand import hand
from scores import scoreengine

h = hand()
h.dice[0].held = True
print [d.value for d in h.dice]
print [d.held for d in h.dice]

se = scoreengine()
print ["%s: %d" % (s.title, s.score(h)) for s in se.get_possible(h)]

h.roll()
print [d.value for d in h.dice]

h.unhold_all()
print [d.value for d in h.dice]
