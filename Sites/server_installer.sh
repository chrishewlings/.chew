#!/usr/bin/env bash

if [ -a $HOME/Library/.server_installed ]; then
	printf "\nServer is already installed.\nTo forcibly reinstall it, please rerun this script with --force appended.\n\n"
	exit
fi

export PYTHONPATH="$HOME/Library/Python/2.7"
mkdir -p $PYTHONPATH
mkdir "$HOME/Sites"
cd $HOME
export PATH="$PATH:$HOME/bin"
#ln -s $PYTHONPATH $HOME/bin
easy_install --install-dir $PYTHONPATH openpyxl
touch Library/.server_installed

cd ~/Sites/
python -m CGIHTTPServer > /dev/null 2>&1 &
disown %1