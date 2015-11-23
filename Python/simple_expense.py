#!/usr/bin/env python

import sys, csv
from decimal import *
from pprint import *

billList = [['Name of Bill', '$ Amount', 'Ola paid?', 'Chris paid?']]

subtotalOla = Decimal('0.00')
subtotalChris = Decimal('0.00')
running = True
billCtr = 0

def round_decimal(x):
	return x.quantize(Decimal(".01"), rounding=ROUND_HALF_UP)

def menu(list, question):
    for entry in list:
        print 1 + list.index(entry),
        print ") " + entry
    return raw_input(question)

def finish():
	print "Ola's subtotal is " + str(round_decimal(subtotalOla))
	print "Chris' subtotal is " + str(round_decimal(subtotalChris))

	pprint(billList)
	print str(billCtr) + " bills were entered for calculation."


	if subtotalOla > subtotalChris:
		amtToPay = subtotalOla - subtotalChris
		print "\n\nOla owes Chris : \033[1;31m" + str(round_decimal(amtToPay))
	if subtotalChris > subtotalOla:
		amtToPay = subtotalChris - subtotalOla
		print "\n\nChris owes Ola : \033[1;31m" + str(round_decimal(amtToPay))

	sys.exit(0)


while running == True:
	chrisPaid = False
	olaPaid = False
	print str(billCtr) + " bills have been entered.\n\n"
	billAmt = raw_input("Enter the amount of the bill  > ")
	billName = raw_input("Enter a name for the bill > ")
	if billAmt == '0':
		finish()
	billAmt = Decimal(billAmt)
	whoPaid = menu(['Chris', 'Ola', 'Both', 'Neither'], "who paid the bill? ")
	if whoPaid == '1':
		subtotalOla += (billAmt/2)
		olaPaid = True
	elif whoPaid == '2':
		subtotalChris += (billAmt/2)
		chrisPaid = True
	elif whoPaid == '3':
		pass
	elif whoPaid == '4':
		subtotalOla += (billAmt/2)
		subtotalChris += (billAmt/2)
		olaPaid, chrisPaid = True, True
	billCtr += 1
	billList.append([billName, str(billAmt), olaPaid, chrisPaid])



