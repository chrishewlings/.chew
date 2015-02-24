#!/usr/bin/env python

import os, sys, subprocess

homedir = os.getenv("HOME")
local_python_path = homedir + "Library/Python/"

# check for installed python modules

def check_installed_modules():
	try:
		import openpyxl, keyring
		os.path.isdir(local_python_path)
	except: 
		print("Necessary python modules are not installed. Press any key to install them.")
		raw_input(">")
		install_modules(["openpyxl, keyring"])

# install missing modules

def install_modules(modules):

	if (isinstance(modules, list)):
		for element in modules:
			subprocess.call("easy_install", "--install-dir", local_python_path, element)
		if(not(os.path.isdir(local_python_path))):
			os.mkdir(local_python_path, 0755)
		if(os.getenv("PYTHONPATH") == None):
			path = '''export PYTHONPATH="$HOME/Library/Python/"\n'''
			dest = homedir + "/.bash_profile"
			f = open(dest, 'a')
			f.write(path)
			f.close()
			
	else:
		print("This function only takes lists.")
		sys.exit("255")
