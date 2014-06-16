#!/usr/bin/env python
# -*- coding=utf-8 -*-

# script to make a usb drive contain your mail database and whatnot

import os, sys, subprocess
from os.path import *
#subprocess.call('killall Mail && sleep 3')

def makeExistingDirsLocal(pathList):
	for i in pathList:
		i = expanduser(i)
		if isdir(i) == True:
			localName = i + '.local'
			#os.rename(i, localName)
			print(i, localName)
			
localDirs = ['~/Library/Containers/com.apple.mail/Data/Library/Caches/com.apple.mail',
'~/Library/Containers/com.apple.mail/Data/Library/Mail',
'~/Library/Mail']
makeExistingDirsLocal(localDirs)

def movePreferences(prefFiles):
	for i in prefFiles:
		i = expanduser(i)
		if isdir(i) == True:
			localName = i + '.local'
			print(i, localName)

prefFiles = ['~/Library/Containers/com.apple.mail/Data/Library/Preferences/com.apple.Mail.plist']

movePreferences(prefFiles)

## stopping here. =)