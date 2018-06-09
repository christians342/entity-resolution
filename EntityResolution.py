import xml.etree.ElementTree as ET

tree = ET.parse('cora-all-id.xml')
root = tree.getroot()

for child in root:
    print(child)
    
