#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, errno, subprocess

newFileList = []

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

def unpackPaths(fileList):
	# unpack paths correctly for current user

	for value in fileList:
		newFileList.append(os.path.expanduser(value))
	return newFileList


def allDoneByeBye():
	raw_input("The script has finished executing.  Please close any important files and press any key to reboot the system. ")
	subprocess.call(["shutdown","-r", "now"])
	


# ask for root privileges
'''
if os.geteuid() != 0:
	print("\nThis script requires root privileges. Please run it preceded by sudo, and enter your administrator password when prompted. \n")
	sys.exit(1)
'''

# define which files to remove, can be appended later if needed

genieoFiles = ['~/Library/Application Support/com.genieoinnovation.Installer/',
'~/Library/Application Support/Genieo/',
'~/Library/LaunchAgents/com.genieo.completer.download.plist',
'~/Library/LaunchAgents/com.genieo.completer.update.plist',
'/Library/LaunchAgents/com.genieoinnovation.macextension.plist',
'/Library/LaunchAgents/com.genieoinnovation.macextension.client.plist',
'/Library/LaunchAgents/com.genieo.engine.plist',
'/Library/LaunchAgents/com.genieo.completer.update.plist',
'/Library/LaunchDaemons/com.genieoinnovation.macextension.client.plist',
'/Library/PrivilegedHelperTools/com.genieoinnovation.macextension.client',
'/Library/Frameworks/GenieoExtra.framework',
'/usr/lib/libgenkit.dylib',
'/usr/lib/libgenkitsa.dylib',
'/usr/lib/libimckit.dylib',
'/usr/lib/libimckitsa.dylib',
'/Applications/Genieo',
'/Applications/Uninstall Genieo',
'/Applications/Uninstall IM Completer.app',
'/Application/InstallMac']

vsearchFiles =  ['/Library/LaunchAgents/com.vsearch.agent.plist',
'/Library/LaunchDaemons/com.vsearch.daemon.plist',
'/Library/LaunchDaemons/com.vsearch.helper.plist',
'/System/Library/Frameworks/VSearch.framework',
'/Library/Application Support/VSearch']

conduitFiles = ['/Library/InputManagers/CTLoader/',
'/Library/LaunchAgents/com.conduit.loader.agent.plist',
'/Library/LaunchDaemons/com.perion.searchprotectd.plist',
'/Library/Application Support/SIMBL/Plugins/CT2285220.bundle',
'/Library/Application Support/Conduit/',
'/Applications/SearchProtect.app',
'/Applications/SearchProtect/',
'~/Library/Application Support/Conduit/',
'~/Library/Internet Plug-Ins/ConduitNPAPIPlugin.plugin',
'~/Library/Internet Plug-Ins/TroviNPAPIPlugin.plugin',
'~/Conduit/',
'~/Trovi/']

#spigotFiles = ['~/Library/Application Support/Spigot/']
# need a wildcard for anything with slick savings, ebay shopping assistant, etc

# prompt the user to restart the system
