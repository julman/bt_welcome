import bluetooth
import time

import xml.etree.ElementTree as ET
import xml.etree.Element
tree = ET.parse('macs.xml')
root = tree.getroot()
root.append(Element('actor', {name:"bob", mac:"23:f3:23:f3:23", modDT:"", mp3:"song.mp3"}))
