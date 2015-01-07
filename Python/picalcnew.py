#! /usr/bin/env python

# program to count decimal digits of pi using a really slow series

import math
piVar = 4 
x = 3

#precision

for i in xrange(1, 200000):
	piVar = piVar - (4.0/x) + (4.0/(x+2))
	x = x + 4
	print(piVar)

# 1m02s to calculate 200000 iterations