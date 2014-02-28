#!c:\Python27\python.exe

import cgi,cgitb

print "Context-Type: text/html\n"
print 

try:
	form  = cgi.FieldStorage()
	#get all the inputs by getlist()
	colors = form.getlist('color')

	print "Context-Type: text/html\n"
	print '<html><body>'
	print 'The colors list:',colors
	for color in colors:
		print '<p>', cgi.escape(color),'</p>'
	print '</body><html>' 
except:
	cgitb.handler()