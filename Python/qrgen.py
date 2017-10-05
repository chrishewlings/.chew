#!/usr/bin/env python

import urllib2, sys, subprocess


transformed_args = []
filename_proto = '/var/tmp/'
for arg in sys.argv[1:]:
	transformed_args.append('https://chart.googleapis.com/chart?cht=qr&chs=200x200&chl=' + str(arg).upper())

for i,arg in enumerate(transformed_args):

	obj = urllib2.urlopen(arg)
	realfilename = filename_proto + sys.argv[i+1] + '.png'
	
	with open(realfilename,'w') as f:
		f.write(obj.read())
	
	subprocess.call(["open",realfilename])	
