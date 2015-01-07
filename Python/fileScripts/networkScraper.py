#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys, subprocess
from pprint import pprint

var = subprocess.check_output('networksetup -getinfo Ethernet', shell=True).splitlines()

del(var[0])
networkInfo = {}

for x in var:
	index = x.find(':')
	index +=1
	key = x[0:index-1]
	value = x[index:len(x)]
	networkInfo[key] = value
	
pprint(networkInfo)

	
	

