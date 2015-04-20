#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re, sys, subprocess
from decimal import *

subprocess.call("clear")

getcontext().prec = 2
peopleToSplit = {'Ola' : Decimal(0.00) , 'Chris' : Decimal(0.00), 'Both' : Decimal(0.00)}




cashMoney = re.compile('|'.join([
  r'^\$?(\d*\.\d{1,2})$',  # e.g., $.50, .50, $1.50, $.5, .5
  r'^\$?(\d+)$',           # e.g., $500, $5, 500, 5
  r'^\$(\d+\.?)$',         # e.g., $5.
]))

# class constructor to permit using c-style case statements instead of clunky elifs

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: 
            self.fall = True
            return True
        else:
            return False

#function to create a menu with numbered choices
def menu(list, question):
    for entry in list:
        print 1 + list.index(entry),
        print ") " + entry
    return raw_input(question)

def askForAmount():
	while True:
		amount = raw_input("Enter the amount of the bill to calculate, in dollars & cents. \n\n> ")
		if cashMoney.match(amount):
			return Decimal(amount)
			break
		else:
			print "try again."

def whoAlreadyPaid(billAmount):
	choice = menu(peopleToSplit, "Who already paid this bill?")
	for case in switch(choice):
		if case('1'): #chris 
			peopleToSplit('Ola') += (billAmount / 2)
			break
		if case('2'): # ola
			peopleToSplit('Chris') += (billAmount / 2)
			break
		if case('3'): #both
			pass
			break
		if case(''): #nothing
			print("make a choice!")	
			break
#askForAmount() 
whoAlreadyPaid(Decimal('164.50')
