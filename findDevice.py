import bluetooth

adress = None

devices = bluetooth.discover_devices()
if(len(devices)>1):
	print "only one device at a time bitches!"
else:
	if(len(devices)<1):
		print "need at least one devices to be discoerable!"
	else:
	
		for discovered_address in devices:
			print "found " + discovered_address
