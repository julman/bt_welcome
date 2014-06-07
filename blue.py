import bluetooth
import time
result = bluetooth.lookup_name('10:D5:42:BB:48:5F', timeout=5)
if(result != None):
	print "im here!"
else:
	print "im not here :("


