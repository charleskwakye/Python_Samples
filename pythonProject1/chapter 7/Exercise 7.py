with open('Files Chapter 7/playlist.txt', encoding='UTF-8') as file:
    lines = file.readlines()
    lines.sort()

for line in lines:
    record = line.split(';')
    print(record[0],'\t',record[1].upper(),'(' + record[2].lower().rstrip()+')')
    