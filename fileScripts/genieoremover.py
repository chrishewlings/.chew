#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, errno, subprocess



# definitions
def removeElementsNicely(list):
	
	for element in list:
		try:
			os.remove(element)
		except OSError as e:
			if e.errno == 2:
				pass # fail silently and pass if file does not exist
			elif e.errno == 1:
				os.rmdir(element) #fail silently and attmept to remove element if it a directory
				pass

def displayWindow():
	subprocess.call('osascript -e "display dialog')
	


# ask for root privileges
'''
if os.geteuid() != 0:
	print("\nThis script requires root privileges. Please run it preceded by sudo, and enter your administrator password when prompted. \n")
	sys.exit(1)
'''

# define which files to remove

userLibraryFiles = ['~/Library/Application Support/com.genieoinnovation.Installer/',
'~/Library/Application Support/Genieo/',
'~/Library/LaunchAgents/com.genieo.completer.download.plist',
'~/Library/LaunchAgents/com.genieo.completer.update.plist']

rootLibraryFiles = ['/Library/LaunchAgents/com.genieoinnovation.macextension.plist',
'/Library/LaunchAgents/com.genieoinnovation.macextension.client.plist',
'/Library/LaunchAgents/com.genieo.engine.plist',
'/Library/LaunchAgents/com.genieo.completer.update.plist',
'/Library/LaunchDaemons/com.genieoinnovation.macextension.client.plist',
'/Library/PrivilegedHelperTools/com.genieoinnovation.macextension.client',
'/Library/Frameworks/GenieoExtra.framework']

usrlibFiles = ['/usr/lib/libgenkit.dylib',
'/usr/lib/libgenkitsa.dylib',
'/usr/lib/libimckit.dylib',
'/usr/lib/libimckitsa.dylib']

applicationFiles = ['/Applications/Genieo',
'/Applications/Uninstall Genieo',
'/Applications/Uninstall IM Completer.app']

# unpack paths correctly for current user

for index, value in enumerate(userLibraryFiles):
	userLibraryFiles[index] = os.path.expanduser(userLibraryFiles[index])

			
#removeElementsNicely(userLibraryFiles)
#removeElementsNicely(rootLibraryFiles)
#removeElementsNicely(usrlibFiles)
#removeElementsNicely(applicationFiles)

displayWindow()
# prompt the user to restart the system
