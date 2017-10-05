#!/usr/bin/env bash

style_colorRed=$(tput setaf 1)
style_colorGreen=$(tput setaf 2)
style_reset=$(tput sgr0)


status_OK="[${style_colorGreen} OK ${style_reset}]"
status_fail="[${style_colorRed} FAIL ${style_reset}]"


logger(){

	message="$1"
	status="$2"
	
	let adjustment_rightAlign=$(tput cols)-${#message}+${#style_colorRed}+${#style_reset}

	printf "%s%${adjustment_rightAlign}s" "$message" "$status"; printf "\n"

}

logger "This is a pretty long thing" "$status_OK"
logger "This is hopefully problematic" "$status_fail"

