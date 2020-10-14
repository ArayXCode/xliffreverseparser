import sys
import os
import fs

from xml.etree import ElementTree as ET


#Create tree from .xlf File //TODO: dateinput variabel gestalten
tree = ET.parse('country_data.xlf')
root = tree.getroot()

#Find all trans-units with target state=needs-translation
for file in root.iter():
    if file.tag == '{urn:oasis:names:tc:xliff:document:1.2}group' :
        if file.get('id'):
            for trans_unit in file.findall('{urn:oasis:names:tc:xliff:document:1.2}trans-unit'):
                target = trans_unit.find('{urn:oasis:names:tc:xliff:document:1.2}target')
                try:
                    if target.get('state') == 'needs-translation':
                        source = trans_unit.find('{urn:oasis:names:tc:xliff:document:1.2}source')
                        if source is not None:
                            print(source.text) #//TODO: Suche und Ersetzung ion Zieldatei einbauen
                except:
                    print("no target found!")
