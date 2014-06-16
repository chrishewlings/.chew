#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Menuing class adapted (and somewhat modified) from Goncalo Gomes, http://promisc.org
#

#from signal import *
#signal(SIGINT, SIG_IGN)

from curses import *
from sys import exit
import os, traceback, atexit, time

## menu class and method definition

class cmenu(object):
    datum = {}
    ordered = []
    caret = 0

    def __init__(self, options, title):
        initscr()
        start_color()
        init_pair(1, COLOR_RED, COLOR_WHITE)
        curs_set(0)
        cbreak()
        noecho()
        self.screen = initscr()
        self.screen.keypad(1)

        self.h = color_pair(1)
        self.n = A_NORMAL

        for item in options:
            k, v = item.items()[0]
            self.datum[k] = v
            self.ordered.append(k)

        self.title = title

        atexit.register(self.cleanup)

    def cleanup(self):
        doupdate()
        endwin()

    def upKey(self):
        if self.caret == (len(self.ordered) - 1):
            self.caret = 0
        else:
            self.caret += 1

    def downKey(self):
        if self.caret <= 0:
            self.caret = len(self.ordered) - 1
        else:
            self.caret -= 1

    def display(self):
        screen = self.screen


        while True:
            screen.clear()
            screen.border(0)
            screen.addstr(2, 2, self.title, A_STANDOUT|A_BOLD)
            screen.addstr(4, 2, "Please select an option.", A_BOLD)
            screen.addstr(5, 2, "Use arrow keys to navigate.")

            ckey = None
            func = None

            while ckey != ord('\n'):
                for n in range(0, len(self.ordered)):
                    optn = self.ordered[n]

                    if n != self.caret:
                        screen.addstr(7 + n, 4, "%d. %s" % (n, optn), self.n)
                    else:
                        screen.addstr(7 + n, 4, "%d. %s" % (n, optn), self.h)
                screen.refresh()

                ckey = screen.getch()

                if ckey == 258:
                    self.upKey()

                if ckey == 259:
                    self.downKey()

            ckey = 0
            self.cleanup()
            if self.caret >= 0 and self.caret < len(self.ordered):
                self.datum[self.ordered[self.caret]]()
                self.caret = -1
            else:
                beep()


## function definitions

# define what type of printer is to be added

''' REDO WITH CURSES
def askPrinterType(): # define what type of printer is to be added
    while True:
        printerTypes = ["Zebra Label Printer","Lexmark Laser Printer"]
        choice = menu(printerTypes, "What is the type of printer you would like to add? ")
        for case in switch(choice):
            if case('1'):
                name = "ZEBRA"
                return name
            if case('2'):
                name = "LASER"
                return name
            if case():
                print("Invalid choice, please choose again.")

'''

def askIpAddress(): # define what the IP address of the printer is, as well as sanity check valid IPv4 input using regex
    while True:
        ipAddress = raw_input("What is the IP address of the printer you would like to add? ")
        if match('^(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))\.(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))\.(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))\.(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))$', ipAddress):
            return ipAddress
        print("\n Invalid IP address, please try again. \n")


def askStoreNumber(): # define store number for prefix when adding printer + sanity check for proper input

    while True:
        storeNumber = raw_input("What is your store number? (with the leading R) ")
        if match('^[R]\d\d\d$', storeNumber):
            return storeNumber
        else:
            print("Invalid store number, please try again. \n")


''' REDO WITH CURSES AND ELIFS
def askPrinterLocation(): # define a string with the printer's location that's concise enough to be a suffix 

    while True:
        potentialLocations = ["Genius Room", "Genius Room 2", "Back of House", "360 Bar Left", "360 Bar Right", "Getting Started"]
        locationMenuChoice = menu(potentialLocations, "Where will this printer be located? ")
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
'''

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

# Checks to see if the script has received a file as its input and sets flow control to interactive or automated mode
''' EXPERIMENTAL
def checkFileInput():
    
    try:
        sys.argv[1]
        automatedMode()
    except IndexError:
        interactiveMode()
'''

def interactiveMode():
    while True:

        global printerType
        storeNumber = askStoreNumber()
        printerType = askPrinterType()
        printerLocation = askPrinterLocation()
        fullIp = askIpAddress()
        fullName = storeNumber + "_" + printerType + "_" + printerLocation
        addPrinter( fullName, printerLocation, fullIp )
        call("clear")
        
        while True: #redo with curses?
            choice = raw_input("Successfully added and configured the selected printer. Would you like to configure another? Y/N ")
            if choice == "Y" or choice == "y":
                call("clear")
                break
            elif choice == "N" or choice == "n":
                call("clear")
                exit(0)
            else:
                call("clear")
                print("Invalid choice, please choose again.\n\n")

def automatedMode():
    print("automatedModeplaceholder")
    exit(0)


def definitionMode():
    print("definitionModeplaceholder")
    exit(0)

def helpScreen():
    print("helpscreenplaceholder")
    exit(0)

def errorExit():
    exit(1)

try:
    mainMenu = cmenu([
        { "Add a new printer": interactiveMode },
        { "Use an existing printer configuration file": definitionMode },
        { "Create a new printer configuration file": automatedMode },
        { "Help": helpScreen },
        { "Exit": errorExit },
        ], title="Printer Configuration Tool")
    mainMenu.display()

except SystemExit:
    pass
else:
    #log(traceback.format_exc())
    mainMenu.cleanup()