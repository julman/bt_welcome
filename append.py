from xml.etree.ElementTree import fromstring, ElementTree, Element
import xml.etree.ElementTree as ET
import xml.dom.minidom

tree = ET.parse('macs.xml')
root = tree.getroot()
newActorNode = ET.Element('actor')
newName = ET.Element('name')
newName.text = 'bobbbobobo'
newMac = ET.Element('mac')
newMac.text = '12:124:12:12:2d'
newModDT = ET.Element('modDT')
newModDT.text = ''
newMp3 = ET.Element('mp3')
newMp3.text = 'sounds/indiana.mp3'
newActorNode.append(newName)
newActorNode.append(newMac)
newActorNode.append(newModDT)
newActorNode.append(newMp3)
root.append(newActorNode)
tree.write('macs.xml')
