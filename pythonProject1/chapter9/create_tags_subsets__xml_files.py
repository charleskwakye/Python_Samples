import xml.etree.ElementTree as ET
root = ET.Element('countries')  # Declare root tag

finland = ET.Element('country')  # Declare tag
root.append(finland)  # Add tag to root
finland.text = 'Finland'  # Add text to tag

sweden = ET.Element('country')
root.append(sweden)
sweden.text = 'Sweden'
# Alternative way (I prefer this)
ireland = ET.SubElement(root, 'country')
ireland.text = 'Ireland'


konongo = ET.SubElement(ireland, 'Konongo') # Making a sub element of Ireland
konongo.text = 'Konongo'
konongo.set('City', 'yes')  # making an attribute

tree = ET.ElementTree(root)
tree.write('Files chapter 9/counties.xml', encoding='utf-8', xml_declaration=True)

