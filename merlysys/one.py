#!c:\Python27\python.exe

import cgi,cgitb
import smtplib


try:
	form  = cgi.FieldStorage()
	#get all the inputs by getlist()
	maths = form.getfirst('maths','none')
	physics = form.getfirst('physics','none')
	maths= cgi.escape(maths)
	physics = cgi.escape(physics)
	print """\
	Content-Type: text/html\n
	<html><body>
	<p>The subjects you have choosen are '{0}' and '{1}'</p>
	</body>
	<html>
	""".format(maths,physics)
except:
	cgitb.handler()


