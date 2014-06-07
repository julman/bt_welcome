import bluetooth
import time
result = bluetooth.lookup_name('', timeout=5)
if(result != None):
	print "im here!"
else:
	print "im not here :("


