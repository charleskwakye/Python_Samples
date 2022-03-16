with open('Files Chapter 7/first_names.txt') as file:
    print(file.read()) # part a, print entire contents

    # part b use readline()
    total_number = 0
    number_z = 0
    name = file.readline()
    while name:
        total_number += 1
        if 'z' in name.lower():
            number_z +=1
            print(name.rstrip())
        name = file.readline()
print('There are', total_number, 'first names in the file.')
print(number_z, 'of which contain a letter z.')

