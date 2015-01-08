#!/bin/bash


directory="$HOME/.dotfiles"
backup_existing="$HOME/.dotfiles_old"

files="bashrc vimrc bash_profile bash_functions"

mkdir -p $backup_existing

cd $directory

for file in $files; do
		mv ~/.$file $backup_existing
		ln -s $directory/$file ~/.$file
done
