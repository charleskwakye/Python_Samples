with open('Files Chapter 7/schedule.txt') as file:
    all_lines = file.readlines()
    for line in all_lines:
        if line != '\n':
            record = line.split(';')
            print(record[0], record[2].rstrip(), record[1])