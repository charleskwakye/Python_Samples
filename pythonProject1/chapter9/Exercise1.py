import xml.etree.ElementTree as ET

xmlDoc = ET.parse('Files chapter 9/plants.xml')
root = xmlDoc.getroot()
counter = 0
for plants in root:
    if plants.find('light').text == 'SUN':
        counter+=1
        print('Plant', counter,':',plants.find('common').text,'('+plants.find('botanical').text.capitalize()+')')
