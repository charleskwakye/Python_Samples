import xml.etree.ElementTree as ET
xmlDoc = ET.parse('Files chapter 9/drugs.xml')
root = xmlDoc.getroot()

for leaflet in root:
    for names in leaflet.findall('name'):       # for name in each leaflet (names)
        names.text = names.text.upper()         # this names should be uppercase
    for pharmaceutical_forms in leaflet.findall('pharmaceutical_forms'):  # for phamarcy in leaftlet find all phamarcy
        leaflet.remove(pharmaceutical_forms)                # remove all phamarcy and sub element

xmlDoc.write('Files chapter 9/drugs_changes.xml')
