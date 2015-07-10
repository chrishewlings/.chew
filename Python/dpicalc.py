#!/usr/bin/python
from math import *

def dpiCalc(horPixels,vertPixels,displayDiagSize):
	hypotenuse = sqrt(horPixels**2 + vertPixels**2)
	return hypotenuse / displayDiagSize
	
def ask():
	length = input("What is the width of the display, in pixels?")
	height = input("What is the height of the display, in pixels?")
	diagonal = input("What is the diagonal span of the display, in inches?")
	print "The PPI of this display is " + str(dpiCalc(length, height, diagonal))

ask()