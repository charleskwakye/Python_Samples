import xml.etree.ElementTree as ET
xmlDoc = ET.parse('Files chapter 9/cinemas.xml')
root =xmlDoc.getroot()
print('Bioscopen in Antwerpen')


for cinemas in root:
    print(cinemas.find('naam').text)
    print(cinemas.find('straat').text, cinemas.find('huisnummer').text)
    print(cinemas.find('postcode').text, cinemas.find('district').text, '\n')
