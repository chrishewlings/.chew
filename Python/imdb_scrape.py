#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import sys, urllib2, re, json

if len(sys.argv) == 1:
    print "This script requires an argument."
    sys.exit(1)

filmTitle = sys.argv[1]
raw_string = re.compile(r' ')
searchString = raw_string.sub('+', filmTitle)
#print searchString

url = "http://www.imdbapi.com/?t=" + searchString

request = urllib2.Request(url)

response = json.load(urllib2.urlopen(request))
print response["Plot"]
