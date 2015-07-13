#!/usr/bin/env python

import os, mutagen.mp3
cwd = "/Users/chrishewlings/Desktop/Documents"
os.chdir(cwd)


def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

for item in listdir_nohidden(cwd):
	metadata = mutagen.mp3.Open(item)
	try:
		title, podcast_name = str(metadata['TIT2']), str(metadata['TPE1'])
	except KeyError:
		title, podcast_name = " ", " "
	namestring = podcast_name + unicode(" - ") + title + unicode(".mp3")
	os.rename(item, namestring)
	
