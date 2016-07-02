#!/usr/bin/env python

import curses
import subprocess
import os



# Variables

global systemUnitFilePath = '/System/Library/LaunchDaemons'

global targets = { 'basic': ['com.apple.taskgated'],
            'directory': ['basic','com.apple.opendirectoryd'],
            'wiredNetwork': ['basic','com.apple.configd'],
            'wirelessNetwork': ['basic'],
            }

# Function definitions

def launchDaemonExec(domain,unitName):
    unitFileAbsPath = systemUnitFilePath + '/' + unitName + '.plist'

    subprocess.call(['launchctl','bootstrap',domain,unitFileAbsPath])
    subprocess.call(['launchctl','kickstart','system/' + unitBaseName])


def main(screen):
  screen.border(2)
  screen.addstr(2,2,"Please make a selection!")
  screen.addstr(4,4,"1 - Reset a user password")
  screen.addstr(5,4,"2 - Decode automatic login password")
  screen.addstr(6,4,"3 - Enable ethernet interface (if present)")
  screen.addstr(7,4,"4 - Enable wifi interface (if present)")
  screen.addstr(11,4,"0 - Quit")

  screen.refresh()

  screen.getch()



if __name__=='__main__':
  curses.wrapper(main)
