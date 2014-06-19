import bluetooth
from xml.etree.ElementTree import fromstring, ElementTree, Element
import xml.etree.ElementTree as ET

def get_name():
	name = input('Enter your name: ')
	print('Hello' + name)
	return name

def get_song():
	song = input('Enter your chosen song: ')
	print('the song you chose is:' + song)
	return song

def put_in_xml(name, song, mac):
	tree = ET.parse('macs.xml')
	root = tree.getroot()
	newActorNode = ET.Element('actor')
	newName = ET.Element('name')
	newName.text = name
	newMac = ET.Element('mac')
	newMac.text = mac
	newModDT = ET.Element('modDT')
	newModDT.text = ''
	newMp3 = ET.Element('mp3')
	newMp3.text = song
	newActorNode.append(newName)
	newActorNode.append(newMac)
	newActorNode.append(newModDT)
	newActorNode.append(newMp3)
	root.append(newActorNode)
	tree.write('macs.xml')
	print "you done!"

devices = bluetooth.discover_devices()
if(len(devices)>1):
	print "Only one device at a time, bitches!"
else:
	if(len(devices)<1):
		print "Need at least one devices to be discoverable!"
	else:

		for discovered_address in devices:
			print "found " + discovered_address
			name = get_name()
			song = get_song()
			put_in_xml(name, song, discovered_address)
