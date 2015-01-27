#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os, sys, subprocess, curses
'''
if os.isdir(/Volumes/UYD4LIFE/) == False:
	print('Please mount the DMG file with your SSH key files.')
	sys.exit()


boxList = ['Helios','Icarus','Zeus']
sshParameters = { 'portNumber' : '',
'hostName' : '',
'''

def get_param(prompt_string):
     win.clear()
     win.border(0)
     win.addstr(2, 2, prompt_string)
     win.refresh()
     input = win.getstr(10, 10, 60)
     return input
	 



def mainMenu(screen):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
	screen.bkgd(curses.color_pair(1))
	screen.refresh()

	win = curses.newwin(10, 60, 1, 1)
	win.bkgd(curses.color_pair(1))
	win.box()
	win.addstr(2, 2, "Please select a server to connect via SSH.", curses.A_STANDOUT )
	win.addstr(4, 2, "1. Helios", curses.color_pair(2))
	win.addstr(5, 2, "2. Icarus", curses.color_pair(2))
	win.addstr(6, 2, "3. Zeus", curses.color_pair(2))
	win.refresh()
	c = screen.getch()
	

try:
	curses.wrapper(mainMenu)
except KeyboardInterrupt:
 	exit()
 	