#!/usr/bin/env python

import urllib2, random, sys

class colors:
	green = '\033[92m'
	red = '\033[91m'
	normal = '\033[0m'

with open('./revised_list') as file:
	names = list(file)
	
	for i, x in enumerate(names):
		names[i] = 'http://' + names[i][:-1]

	random.shuffle(names)
	
	for item in names:
		try:
			element = urllib2.urlopen(item, timeout=5)
			if element.getcode() == 200:
				print(colors.green + "{} has an HTTP server on port 80. ".format(item) + colors.normal)
		except urllib2.URLError as e:
			if sys.stderr.isatty():
				print(colors.red + 'Host not up, or not responding. ({})'.format(item) + colors.normal)
			else:
				sys.stderr.write('Host down or not responding.\t{}\n'.format(item) + colors.normal)


