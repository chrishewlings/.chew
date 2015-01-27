#!/usr/bin/env python
# -*- coding: utf-8 -*-

# when fed a properly formatted csv file of sap inventory, spits out divided by page

import csv, sys
from pprint import *
from openpyxl import Workbook

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
		if columns[0] in listofmodularparts and columns[3] == '252':
			modularRTW.append(columns[0:3])
			deletionindex.append(i)
			
	# make list of adapters
	for i, columns in enumerate(inventory):
		if columns[0] in listofadapters and columns[3] == '252':
			adapterRTW.append(columns[0:3])
			deletionindex.append(i)

	# make list of envelopes
	for i, columns in enumerate(inventory):
		if columns[0] in listofenvelopes and columns[3] == '252':
			envelopeRTW.append(columns[0:3])
			deletionindex.append(i)

	# make list of ipods

	for i, columns in enumerate(inventory):
		if "IPOD" in columns[2] and columns[3] == '252':
			iPodRTW.append(columns[0:3])
			deletionindex.append(i)

	# make list of iphones

	for i, columns in enumerate(inventory):
		if "IPHONE" in columns[2] and columns[0] not in listofmodularparts and columns[3] == '252':
			iPhoneRTW.append(columns[0:3])
			deletionindex.append(i)

	# make list of ipads

	for i, columns in enumerate(inventory):
		if "IPAD" in columns[2] and columns[3] == '252':
			iPadRTW.append(columns[0:3])
			deletionindex.append(i)


deletionindex = list(set(deletionindex))
for i in reversed(deletionindex):
	del inventory[i]

repairPartsInventory = []
for i, columns in enumerate(inventory):
	if not "661" in columns[0]:
		repairPartsInventory.append(columns[0:3])



wb = Workbook()
sheetToRemove = wb.active

def writeToWorksheet(currentWorkbook, sheetName, whichList):
	a = currentWorkbook.create_sheet()
	a.title = sheetName
	for i in whichList:
		a.append(i)

writeToWorksheet(wb, 'Modular RTW List', modularRTW)
writeToWorksheet(wb, 'Adapter RTW List', adapterRTW)
writeToWorksheet(wb, '661 Envelope RTW List', envelopeRTW)
writeToWorksheet(wb, 'iPhone RTW List', iPhoneRTW)
writeToWorksheet(wb, 'iPod RTW List', iPodRTW)
writeToWorksheet(wb, 'iPad RTW List', iPadRTW)
writeToWorksheet(wb, 'Everything Else', repairPartsInventory)
wb.remove_sheet(sheetToRemove)
wb.save("test.xlsx")

'''
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
'''



					