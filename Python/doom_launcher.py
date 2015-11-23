#!/usr/bin/env python
# -*- coding: utf-8 -*-

import npyscreen, os

modsList = []
argsList = []
modsDirectory = os.path.abspath("/Users/chrishewlings/Desktop")
dirContents = os.listdir(modsDirectory)

for thingie in dirContents:
	if thingie.lower().endswith(('.pk3','.wad','.pk7')):
		modsList.append(thingie)

class MainForm(npyscreen.Form):

    def create(self):
		self.modsDisplayed	= self.add(npyscreen.TitleMultiSelect,
										 name='Which mods to run?',
										 values = modsList,
										 scroll_exit=True,
										 max_height=len(modsList) + 4)

def displayMenu(*args):
	screen = MainForm(name='Launcher')
	screen.edit()
	return screen.modsDisplayed.get_selected_objects()

if __name__ == '__main__':
    selectedValues = npyscreen.wrapper_basic(displayMenu)
    for element in selectedValues:
    	argsList.append(modsDirectory + "/" + element)
    print argsList