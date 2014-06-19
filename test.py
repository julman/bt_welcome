import xml.etree.ElementTree as ET
tree = ET.parse('macs.xml')
root = tree.getroot()
bashcommand = "mplayer"
import subprocess
for child in root:
  print child.find('name').text
  child.find('mac').text
