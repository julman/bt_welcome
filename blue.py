import bluetooth
import time
result = bluetooth.lookup_name('74:45:8A:C6:F2:0C', timeout=5)
if(result != None):
	print "im here!"
else:
	print "im not here :("


