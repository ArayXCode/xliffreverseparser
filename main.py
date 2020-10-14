import sys
import os
from lxml import etree
from xml.etree import ElementTree as ET

tree = ET.parse('country_data.xlf')
root = tree.getroot()

#finde start der gruppierung
for file in root.iter():
    if file.tag == '{urn:oasis:names:tc:xliff:document:1.2}group' :
        if file.get('id'):
            group_start = file

#iteration über alle trans_units, findet den translation state, zurzeit wird er nur gedruckt
try:
    for trans_unit in group_start.findall('{urn:oasis:names:tc:xliff:document:1.2}trans-unit'):
        target = trans_unit.find('{urn:oasis:names:tc:xliff:document:1.2}target')
        if target is not None:
            print(target.get('state'))
except:
    print("Something went wrong!")