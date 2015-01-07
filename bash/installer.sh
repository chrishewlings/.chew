#!/usr/bin/bash

# check if script is running for the first time
if [ -a $HOME/Library/.virtualenvinstalled ]
then
	echo "This script has already been installed."
	exit 255
fi

# check if venv directory is already configured

if [ ! -d "$HOME/venv/" ]; then
mkdir $HOME/venv/
fi

#VAR=
#echo $VAR 
export PATH="$HOME/venv/:$HOME/venv/install/bin/:$PATH" 
export PYTHONPATH="$HOME/venv:$HOME/venv/install/bin:$PYTHONPATH"
echo 'export PYTHONPATH=$HOME/venv/:$HOME/venv/install/bin' >> .bash_profile

#install virtualenv

easy_install --install-dir $HOME/venv/ virtualenv
cd $HOME/venv
virtualenv install

#install xlrd

pip install xlrd
pip install xlwt
pip install xlutils

# add installer confirmation file

touch $HOME/Library/.virtualenvinstalled

#cleanup

chflags hidden $HOME/venv
osascript -e "display dialog \"To activate this script, please add it to your Downloads folder action.\" "

