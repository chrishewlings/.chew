#!/bin/bash
USER_DOWNLOADS="$HOME/Downloads"
USER_APPS="$HOME/Applications"

killall Spotify.app SpotifyWebHelper 2&>1 /dev/null

cd $USER_DOWNLOADS
rm *.dmg *.img *.iso *.app 2&>1 /dev/null


if [ -d $USER_APPS/Spotify.app ]
	then
		rm -rf $USER_APPS/Spotify.app
		osascript -e 'tell application "Finder"' -e 'activate' -e 'display dialog "Please do not install third party software on this system."' -e 'end tell'
fi

mount | grep '/Volumes' | awk '{print $1}'
