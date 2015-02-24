#!/usr/bin/env python

import openpyxl, sys, os
from openpyxl import open_workbook

arguments = sys.argv[1:]
if arguments == []:
	print("This script must be passed arguments in order to function.")
	sys.exit(1)

for x in arguments:
	arg = str(x)
	arg = os.path.abs(arg)

listOfModularParts = ['661-6357', '661-6856', '661-8041', '661-00020', '661-00021', '661-00022', '661-00141', '661-00142', '661-00143', '661-00159', '661-00160', '661-00161']
listofenvelopes = ['C661-4954', '661-6367']
listOfAdapters = ['661-5843', '661-6365', '661-6403', '661-6536', '661-7015', '661-00682']

workbook = open_workbook(filename = arg)
ws = workbook.get_sheet_by_name(name = 'Sheet1')





