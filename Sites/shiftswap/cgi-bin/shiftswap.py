#!/usr/bin/env python

import cgi
import cgitb
cgitb.enable()

class User:
	"""class to hold information regarding sender and receiver of request"""
	def __init__(self, firstName, lastName, requestDate, email):
		self.firstName = firstName
		self.lastName = lastName
		self.requestDate = requestDate
		self.email = email


form = cgi.FieldStorage()
requesterAbsDate = form["requesterDay"].value + "/" + form["requesterMonth"].value + "/" + form["requesterYear"].value
recipientAbsDate = form["recipientDay"].value + "/" + form["recipientMonth"].value + "/" + form["recipientYear"].value

Requester = User(form["yourFirstName"].value, form["yourLastName"].value, requesterAbsDate, form["yourEmail"].value)
Recipient = User(form["theirFirstName"].value, form["theirLastName"].value, recipientAbsDate, form["theirEmail"].value) 
print "Content-Type:text/html\n\n"
print
print "<html>"
print "<TITLE>CGI script output</title>"
print(Requester.__dict__)
print(Recipient.__dict__)