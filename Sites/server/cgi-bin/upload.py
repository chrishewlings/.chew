#!/usr/bin/env python

import cgi, os, re
import cgitb; cgitb.enable()


'''
def validateFileName(userEntry):
	if re.search(r'[^A-Za-z0-9_\-\\\.]',userpath) != []
		os.exit(1)
'''

inputForm = cgi.FieldStorage()
emailAddress = cgi.escape(inputForm.getfirst('emailAddress', 'empty'))
uploadedFile = inputForm['file']

saveName = os.path.basename(uploadedFile.filename)
open('files/' + saveName, 'wb').write(uploadedFile.file.read())


# rendering

print """\
Content-Type: text/html\n
<html><body>
<p>The submitted name was "%s"</p>
</body></html>
""" % saveName



#print(inputForm)
