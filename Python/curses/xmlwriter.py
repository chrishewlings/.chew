#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
from xml.dom import minidom as MD

def makeHumanReadable(elem):
	unparsed = ET.tostring(elem, 'utf-8')
	reparsed = MD.parseString(unparsed)
	return reparsed.toprettyxml(indent="	")

root = ET.Element('root')

child = ET.SubElement(root, 'child')
child.text = 'this child contains text'

child = ET.SubElement(root, 'child')
child.text = 'this child contains text2'

#print ET.tostring(root)
print makeHumanReadable(root)