#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import sys, subprocess, os, shutil, random

arguments = sys.argv[1:]
if arguments == []:
	print("This script must be passed arguments in order to function, e.g. : ./script.py file1 file2")
	sys.exit()





## checks if ~/Desktop/Randomized exists, if not, creates it

if os.path.isdir(os.path.expanduser('~/Desktop/Randomized'))==False:
	subprocess.call('mkdir ~/Desktop/Randomized/', shell=True)


#copies items passed as args to ~/Desktop/Randomized/

for x in sys.argv[1:]:
	shutil.copy(x, os.path.expanduser('~/Desktop/Randomized/'))

# creates a list with filenames in that folder, excluding .DS_Store
fileList = os.listdir(os.path.expanduser('~/Desktop/Randomized/'))
try:
	fileList.remove('.DS_Store') 
except ValueError: pass

# loop that renames files with randomized names
for fileName in fileList:
		
	os.chdir(os.path.expanduser('~/Desktop/Randomized'))
	fileExtension = os.path.splitext(fileName)[1]
	uniqueName = str(random.random())
	uniqueName = uniqueName[2:10]
	uniqueName = uniqueName + fileExtension
	os.rename(fileName, uniqueName)

