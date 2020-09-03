import sys
from lxml import objectify
import pandas as pd
import xml.etree.ElementTree as ET
tree = ET.parse('country.xml')
print(tree)
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)