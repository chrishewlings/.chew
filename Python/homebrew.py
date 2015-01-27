#!/usr/bin/python
# -*- 

import os, shutil, subprocess, sys
from os import path

if path.isdir(path.expanduser('~/usr')) == True:
	print('Homebrew is already installed in this user folder.')
	sys.exit()



shutil.copy('/Volumes/UYD4LIFE/usr.tar.bz2', path.expanduser('~/'))
os.chdir(path.expanduser('~/'))
subprocess.call('tar zxvf usr.tar.bz2 && rm usr.tar.bz2', shell=True)
subprocess.call('echo "export PATH=:~/usr/bin:$PATH" >> .bash_profile', shell=True)
subprocess.call('~/usr/bin/git clone https://github.com/Homebrew/homebrew.git', shell=True)
subprocess.call('ln -s ~/homebrew/bin/brew ~/usr/bin/brew', shell=True)
subprocess.call('chflags nohidden ~/usr/ && chflags nohidden ~/homebrew', shell=True)
os.system('clear')
print("All done, bye bye...\n\n")

sys.exit()