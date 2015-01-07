#! /usr/bin/env python

# made a program that makes squares of numbers arbitrarily... by accident.

import math
squareVar = 1 
x = 3

#precision

for i in xrange(1, 20):
	squareVar = squareVar + x
	x = x+2
	print(squareVar)