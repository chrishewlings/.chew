#!/usr/bin/env python
# -*- coding: utf-8 -*-

import npyscreen, os

doomBinary = os.path.expanduser("~/DOOM/GZDoom.app")
modDirectory = os.path.expanduser("~/Applications")

modsList = os.listdir(modDirectory)

class doomLauncher(npyscreen.NPSAppManaged):
	def onStart(self):
		self.registerForm("Main", MainForm())

class MainForm(npyscreen.Form):
	def create(self):
		self.add(npyscreen.TitleText,
			name='doomBinary')
		self.add(npyscreen.TitleSelectOne,
			name='Select Mods to run: ',
			values = ['test','thing'],
			scroll_exit=True,
			max_height=10)

	def afterEditing(self):
		self.parentApp.setNextForm(None)


		

if __name__ == '__main__':
	app = doomLauncher()
	app.run()