#!/usr/bin/env python
# -*- coding: utf-8 -*-


########################
###                  ###
###    Add Printer   ###
###                  ###
########################

# simple utility to add Zebra/Lexmark printers to BOH stations and admin floaters 
# in an automated and user friendly way

# only tested on OS X 10.8, IS&T GR iMac image as of April 2014

#####################################
###  (C)2014 Chris Hewlings LGPL  ###
###   provided with no warranty   ### 
###                               ###
#####################################


# version 0.1 : initial release
# version 0.2 : added a simple loop that asks if you would like to repeat the script

from subprocess import call
from re import match
import sys
call("clear")

# class constructor to permit using c-style case statements instead of clunky elifs

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False


#function to create a menu with numbered choices
def menu(list, question):
    for entry in list:
        print 1 + list.index(entry),
        print ") " + entry
    return raw_input(question)

# define what type of printer is to be added
def askPrinterType():
    while True:
        printerTypes = ["Zebra Label Printer","Lexmark Laser Printer"]
        choice = menu(printerTypes, "What is the type of printer you would like to add? ")
        for case in switch(choice):
            if case('1'):
                name = "ZEBRA"
                return name
                break
            if case('2'):
                name = "LASER"
                return name
                break
            if case():
                print("Invalid choice, please choose again.")

# define what the IP address of the printer is, as well as sanity check valid IPv4 input using regex
def askIpAddress():
    while True:
        ipAddress = raw_input("What is the IP address of the printer you would like to add? ")
        if match('^(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))\.(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))\.(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))\.(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))$', ipAddress):
            return ipAddress
        print("\n Invalid IP address, please try again. \n")

# define store number for prefix when adding printer + sanity check for proper input
def askStoreNumber():
    while True:
        storeNumber = raw_input("What is your store number? (with the leading R) ")
        if match('^[R]\d\d\d$', storeNumber):
            return storeNumber
        else:
            print("Invalid store number, please try again. \n")

# define a string with the printer's location that's concise enough to be a suffix 
def askPrinterLocation():
    while True:
        potentialLocations = ["Genius Room", "Genius Room 2", "Back of House", "360 Bar Left", "360 Bar Right", "Getting Started"]
        locationMenuChoice = menu(potentialLocations, "Where will this printer be located?")
        for case in switch(locationMenuChoice):
            if case('1'):
                loc = "GR"
                return loc
            if case('2'):
                loc = "GR2"
                return loc
            if case('3'):
                loc = "BOH"
                return loc
            if case('4'):
                loc = "360_L"
                return loc
            if case('5'):
                loc = "360_R"
                return loc
            if case('6'):
                loc = "GS"
                return loc
            if case():
                print "Invalid choice, please choose again."


# generate a PPD file in /tmp/ for the Zebra ZPL printer, which will be wiped out after a reboot, and modifies its settings using a fucking perl hackjob
def generatePpdFile():
    #call(["mkdir", "/tmp/ppd")
    call("ppdc -d /tmp/ /usr/share/cups/drv/sample.drv", shell=True)
    call("perl -p -e 's/w288h360\n/w162h288\n/' /tmp/zebra.ppd > /tmp/zebra_temp.ppd", shell=True)
    call("perl -p -e 's/203dpi\n/300dpi\n/' /tmp/zebra_temp.ppd > /tmp/zebra_tempier.ppd", shell=True)
    call("mv /tmp/zebra_tempier.ppd /tmp/zebra.ppd", shell=True) 

# add the printer to CUPS
def addPrinter(a,b,c):
    
    #printerType = askPrinterType()

    var = [ a, b, c ]
        
    if printerType == 'ZEBRA':
        var[2] =  "lpd://" + var[2]
        generatePpdFile()
        call(["lpadmin", "-p", var[0], "-L", var[1], "-E", "-v", var[2], "-P", "/tmp/zebra.ppd"])
    elif printerType == 'LASER':
        var[2] =  "ipp://" + var[2]
        call(["lpadmin", "-p", var[0], "-L", var[1], "-E", "-v", var[2], "-P", "/Library/Printers/PPDs/Contents/Resources/Lexmark E460dn.gz"])
    else:
        print("this shouldn't happen…")
    
                
while True:
   	
	call('clear')
	storeNumber = askStoreNumber()
	printerType = askPrinterType()
	printerLocation = askPrinterLocation()
	fullIp = askIpAddress()
	fullName = storeNumber + "_" + printerType + "_" + printerLocation
	addPrinter( fullName, printerLocation, fullIp )
	call('clear')
	keepGoing = raw_input('Would you like to add another printer? \n 1) Yes \n 2) No  \n\n')
	if keepGoing == '1':
		continue
	if keepGoing == '2':
		call('clear')
		sys.exit()
	else:
		sys.exit()


		
		




