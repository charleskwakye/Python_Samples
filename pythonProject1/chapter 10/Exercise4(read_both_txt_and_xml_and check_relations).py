import xml.etree.ElementTree as ET

set_xml = set()
set_txt = set()
xmlDoc = ET.parse('Files Chapter 10/games.xml')
root = xmlDoc.getroot()
counter = 0
for game in root.iter('game'):
    set_xml.add(game[1].text)


with open('Files Chapter 10/games.txt', encoding='utf8') as file:
    line = file.readline()
    while line:
        record = line.rstrip().split(',')
        types_game = record[7].strip("''").strip(" ").lower()
        set_txt.add(types_game)
        line = file.readline()

set_intersection = set_txt.intersection(set_xml)
only_txt_set = set_txt - set_xml
only_xml_set = set_xml - set_txt
print('In the txt-file: ', len(set_txt), 'types of games')
print('In the xml-file: ', len(set_xml), 'types of games', '\n')

print('The type that occurs in both files: ')
print(set_intersection, '\n')

print('The type appear only in txt-file: ')
print(set_txt, '\n')

print('The type that only appear in xml-file: ')
print(only_xml_set)