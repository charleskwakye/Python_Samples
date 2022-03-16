import xml.etree.ElementTree as ET
root = ET.Element('compilation')

with open('Files chapter 9/songs.txt') as file:
    lines = file.readlines()


for line in lines:
    record = line.split(';')
    artist_t = record[0]
    song_t = record[1].rstrip()

    track = ET.SubElement(root,'track')
    artist_x = ET.SubElement(track,'artist')
    artist_x.text = artist_t

    song_x = ET.SubElement(track, 'song')
    song_x.text = song_t

tree = ET.ElementTree(root)
tree.write('Files chapter 9/song.xml', encoding='utf-8', xml_declaration=True)