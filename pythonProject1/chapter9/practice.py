import xml.etree.ElementTree as ET
root = ET.Element('compilation')
with open('Files chapter 9/songs.txt', encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    record = line.rstrip().split(';')
    artist_name = record[0]
    song_name = record[1]

    track = ET.SubElement(root,'track')
    artist = ET.SubElement(track, 'artist')
    artist.text = artist_name

    song = ET.SubElement(track,'song')
    song.text = song_name


tree = ET.ElementTree(root)
tree.write('just_created.xml', encoding='utf-8', xml_declaration=True)


