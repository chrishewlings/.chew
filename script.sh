#!/bin/bash

export TERM_FROZEN_STATE="$HOME/Library/Saved Application State/com.apple.Terminal.savedState"
export WORKING_DIR="/var/tmp"

cd $WORKING_DIR
curl -s cloudfront.volitans-software.com/smartutility312.zip | tar -xf- -C . 
open SMART\ Utility/SMART\ Utility.app
sleep 20
killall SMART\ Utility.app
rm -rf "$WORKING_DIR/SMART Utility/"


if [ -d "$TERM_FROZEN_STATE" ]; then
	rm -rf $TERM_FROZEN_STATE
fi



killall Terminal





