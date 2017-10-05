#!/usr/bin/env python

import platform, os, sys, subprocess

#global variables

kernelName, osVersion, kernelVersion = platform.uname()[0] , int(platform.mac_ver()[0].split('.')[1]), platform.uname()[2]



def checkOS(kernelName,osVersion):
	if kernelName != 'Darwin' or osVersion <= 5:
		sys.exit("This tool will only run on Mac OS X 10.6 and up.")



	
