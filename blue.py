import bluetooth
import time

import xml.etree.ElementTree as ET
tree = ET.parse('macs.xml')
root = tree.getroot()
for child in root:
		result = bluetooth.lookup_name(child.find("mac"), timeout=5)
		if(result != None):
			print child.find("name").text . "im here!"
		else:
			print "im not here :("
