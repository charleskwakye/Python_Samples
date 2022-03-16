with open('Files Chapter 7/hamlet.txt', 'r') as input_file:
    with open('hamlet.txt', 'w') as output_file:
        lines = input_file.readlines()
        for item in lines:
            for character in ',.;:?!':
                item = item.replace(character+' ', character+' ')
            output_file.write(item)
        