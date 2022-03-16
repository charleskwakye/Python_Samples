import random
import xml.etree.ElementTree as ET


def read_names():
    chosen_names_list = []
    with open('Files Chapter 12/names.txt') as file:
        line = file.readline()
        while line:
            record = line.rstrip().split('/')
            chosen_name = record[random.randint(0,4)]
            chosen_names_list.append(chosen_name)
            line = file.readline()
            chosen_names_list.sort()
        return chosen_names_list

def read_figures():
    figures_list = []
    xmlDoc = ET.parse('Files Chapter 12/figures.xml')
    root = xmlDoc.getroot()
    for figures in root:
        li_item = figures.find('colour').text + ' ' + figures.find('shape').text
        figures_list.append(li_item)
    return figures_list


#  main pro
names_in_list = read_names()
shape_in_list = read_figures()

print('A figure has been chosen for the following toddlers')
for name in names_in_list:
    print(name,'\t' ,shape_in_list[len(name)])