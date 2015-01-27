#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, errno, subprocess

newFileList = []
rightEdge = os.environ['COLUMNS'] - 1
subprocess.call('clear')

# definitions
def removeElementsNicely(list):
	list = unpackPaths(list)
	for element in list:
		try:
			os.remove(element)
			print("FOUND:" + element + "\033[32m[REMOVED √]\033[0m")
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

def warnUser(message):
	choice = raw_input(message)
	if choice != '':
		sys.exit(1)


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

onlySearchFiles = ['/Library/Application Support/solar',
'/Library/LaunchAgents/com.solar.agent.plist',
'/Library/LaunchDaemons/com.solar.daemon.plist',
'/System/Library/Frameworks/v.framework']

fkCodecFiles = ['~/Library/Application Support/Codec-M',
'~/Library/LaunchAgents/com.codecm.uploader.plist',
'/Applications/Codec-M.app']

chatZumFiles = ['/Applications/ChatZumUninstaller.pkg',
'/Library/Application Support/SIMBL/Plugins/SafariOmnibar.bundle',
'/Library/Internet Plug-Ins/uid.plist',
'/Library/Internet Plug-Ins/zako.plugin']



spigotFiles = ['~/Library/Application Support/Spigot/',
'~/Library/Safari/Extensions/Amazon Shopping Assistant.safariextz',
'~/Library/Safari/Extensions/Searchme.safariextz',
'~/Library/Safari/Extensions/SlickSavings.safariextz']

variousSafariExtensions = ['~/Library/Safari/Extensions/AS-1.0.safariextz',
'~/Library/Safari/Extensions/searchExt.safariextz',
'~/Library/Safari/Extensions/searchme.safariextz',
'~/Library/Safari/Extensions/palmall-1-2.safariextz',
'~/Library/Safari/Extensions/Omnibar-2.safariextz']

warnUser("\033[07m\033[01m\033[31mThis is entirely unsupported and run at your own risk.\nIf any data loss occurs, the creator of this script bears no responsibility; legal, ethical, or otherwise.\033[0m\n\nThis script is designed to remove certain known malware/adware applications from \033[32mMac OS X\033[0m and \033[32mSafari,\033[0m respectively.\nCurrently no removal is performed for \033[32mGoogle Chrome, Firefox, or Opera.\033[0m\nPlease remove any suspect extensions from these applications manually.\n\n\033[04mPress any key to start the removal.\033[0m")
removeElementsNicely(spigotFiles)

# prompt the user to restart the system
