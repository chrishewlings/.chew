#!/bin/bash

sudo -v

while true; do sudo -n true; sleep 60; kill -0 "$$" || exit; done 2>/dev/null &

## pre-requisites

xcode-select --install && read -rsp $'Press any key to continue once the Xcode command line tools have finished installing...\n' -n1 key

## homebrew install 

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

## brew taps

brew tap homebrew/eompletions
brew tap caskroom/fonts

## homebrew formulas

formula_list=("archey" "aria2" "bash" "bash-completion" "brew-cask-completion" "colordiff" "coreutils" "emacs" "gem-completion" "gnupg" "htop" "launchctl-completion" "lbzip2" "mc" "nmap" "p7zip" "pigz" "pixz" "rsync" "speedtest-cli" "ssh-copy-id" "thefuck" "tmux" "trash" "unrar" "vim" "wakeonlan" "wget" "youtube-dl" "xz" "zsh" "zsh-completions" "zsh-syntax-highlighting")

for i in ${formula_list[@]}; do
	brew install "$i"
done

## casks

cask_list=("1password" "alfred" "atom" "animated-gif-quicklook" "aquamacs" "bettertouchtool" "betterzipql" "bonjour-browser" "cyberduck" "dropbox" "flux" "gfxcardstatus" "google-chrome" "grandperspective" "handbrake" "iterm2" "qlcolorcode" "qlimagesize" "qlmarkdown" "qlprettypatch" "qlstephen" "quicklook-csv" "quicklook-json" "sublime-text" "the-unarchiver" "thunderbird" "vlc" "xquartz")

## other non-homebrew things


# var tmp
curl -L -o gdisk.pkg https://sourceforge.net/projects/gptfdisk/files/gptfdisk/1.0.1/gdisk-binaries/gdisk-1.0.1.pkg/download
sudo installer -pkg ./gdisk.pkg -target /


git clone https://github.com/stephenway/monokai.terminal.git # output to var tmp
# open monokai.terminal/Monokai.terminal
# open monokai.terminal/Monokai.itermcolors


defaults write com.apple.Terminal "Default Window Settings" Monokai
defaults write com.apple.Terminal "Startup Window Settings" Monokai
