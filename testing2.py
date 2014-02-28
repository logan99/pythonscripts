#!c:\Python27\python.exe
print "Context-Type: text/html"
print
import cgitb
try:
	f = open('non-exi.txt','r')
except:
	cgitb.handler()