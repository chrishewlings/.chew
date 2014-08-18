#!/usr/bin/env python
# -*- coding: utf-8 -*-

# when fed a properly formatted csv file of sap inventory, spits out divided by page

import csv, sys
from pprint import *

arguments = sys.argv[1:]
if arguments == []:
	print("This script must be passed arguments in order to function.")
	sys.exit(1)

for x in arguments:
	arg = str(x)

listofmodularparts = ['661-6357', '661-6856', '661-8041', '661-00020', '661-00021', '661-00022']
listofadapters = ['661-5843', '661-6365', '661-6403', '661-6536', '661-7015']
listofenvelopes = ['C661-4954', '661-6367']


modularRTW = []
adapterRTW = []
envelopeRTW = []
iPhoneRTW = []
iPodRTW = []
iPadRTW = []

with open(arg, 'r') as csvfile:
	inventoryfromfile = csv.reader(csvfile)
	inventory = []
	deletionindex = []
	
	for i in inventoryfromfile:
		inventory.append(i)


	# make list of modulars

	for i, columns in enumerate(inventory):
		if columns[0] in listofmodularparts:
			modularRTW.append(columns[0:3])
			deletionindex.append(i)
			
	# make list of adapters
	for i, columns in enumerate(inventory):
		if columns[0] in listofadapters:
			adapterRTW.append(columns[0:3])
			deletionindex.append(i)

	# make list of envelopes
	for i, columns in enumerate(inventory):
		if columns[0] in listofenvelopes:
			envelopeRTW.append(columns[0:3])
			deletionindex.append(i)

	# make list of ipods

	for i, columns in enumerate(inventory):
		if "IPOD" in columns[2]:
			iPodRTW.append(columns[0:3])
			deletionindex.append(i)

	# make list of iphones

	for i, columns in enumerate(inventory):
		if "IPHONE" in columns[2] and columns[0] not in listofmodularparts:
			iPhoneRTW.append(columns[0:3])
			deletionindex.append(i)

	# make list of ipads

	for i, columns in enumerate(inventory):
		if "IPAD" in columns[2]:
			iPadRTW.append(columns[0:3])
			deletionindex.append(i)


deletionindex = list(set(deletionindex))
for i in reversed(deletionindex):
	del inventory[i]

repairPartsInventory = inventory

def writeToFile(listname, filename):
	with open(filename, 'w') as x:
		writer = csv.writer(x)
		writer.writerows(listname)

writeToFile(modularRTW,'Modular Parts List.csv')
writeToFile(adapterRTW,'Adapter RTW List.csv')
writeToFile(envelopeRTW, 'Envelope RTW list.csv')
writeToFile(iPhoneRTW,'iPhone RTW List.csv')
writeToFile(iPodRTW, 'iPod RTW List.csv')
writeToFile(iPadRTW, 'iPad RTW List.csv')


#for i in deletionindex:




					
