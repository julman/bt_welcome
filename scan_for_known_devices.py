import bluetooth
import time

import xml.etree.ElementTree as ET
tree = ET.parse('macs.xml')
root = tree.getroot()
import subprocess
for child in root:
		print child.find("mac").text
		result = bluetooth.lookup_name(child.find("mac").text, timeout = 5)
		print result
		if(result != None):
			print child.find("name").text + (" is here!")
			bashcommand = "mplayer " + child.find("mp3").text
			process = subprocess.Popen(bashcommand.split(), stdout=subprocess.PIPE)
			output = process.communicate()[0]
		else:
			print child.find("name").text + " is not here :("
