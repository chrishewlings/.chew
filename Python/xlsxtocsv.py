#!/usr/bin/env python

import os, sys, openpyxl, csv

def xlsx_to_csv(origFile, csvToWrite):
	workbook = openpyxl.load_workbook(origFile)
	sh = workbook.get_active_sheet()
	with open(csvToWrite, 'wb') as file:
		c = csv.writer(file)
		for r in sh.rows:
			c.writerow([cell.value for cell in r])

xlsx_to_csv('/Users/apple/Downloads/export-21.xlsx', 'test.csv')
