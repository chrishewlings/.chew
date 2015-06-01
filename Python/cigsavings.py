#!/usr/bin/env python

import datetime
from decimal import *

fuckups = 4

packCost = Decimal('9.50')
packQuantity = 25

startDate = datetime.date(2014, 12, 31)
todaysDate = datetime.date.today()


amountAvoided = ((todaysDate - startDate).days)*packQuantity

amountAvoided = amountAvoided - fuckups*packQuantity
fuckupCost = fuckups * packCost

amountSaved = (((todaysDate - startDate).days)*packCost) - fuckupCost

print("Hello!\n")

print("You have saved \033[32m$" + str(amountSaved) + " \033[0msince you stopped buying cigarettes.")
print("You have avoided smoking \033[32m" + str(amountAvoided) + " \033[0mcigarettes since you stopped buying packs.")
print("You have fucked up \033[31m" + str(fuckups) + " \033[0mtimes, and spent \033[1;31m$" + str(fuckupCost) + "\033[0m because of it.")
print("\n")

