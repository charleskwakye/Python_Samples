import xml.etree.ElementTree as ET
types_txtfile = set()
types_xmlfile = set()

with open('Files Chapter 10/games.txt', encoding='utf8') as file1:
    line = file1.readline()
    while line:
        record = line.rstrip().split(',')
        types_game = record[-5].strip("''").strip(" ").lower()
        types_txtfile.add(types_game)
        line = file1.readline()
print('In the txt-file:',len(types_txtfile),'types of games')

xmlDoc = ET.parse('Files Chapter 10/games.xml')
root = xmlDoc.getroot()
for game in root.iter('game'):
    types_xmlfile.add(game[1].text.lower())
print('In the xml-file:',len(types_xmlfile),'types of games')

print('\nThe type that occur in both files:')
#print(types_txtfile & types_xmlfile) 3second alternative
print(types_xmlfile.intersection(types_txtfile))

print('\nThe type that only appear in text files:')
#print(types_txtfile - types_xmlfile)
print(types_txtfile.difference(types_xmlfile))

print('\nThe type that only appear in xml files:')
#print(types_xmlfile - types_txtfile)
print(types_xmlfile.difference(types_txtfile))