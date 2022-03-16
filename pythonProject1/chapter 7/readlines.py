with open('Files Chapter 7/schedule.txt') as file:
    all_lines = file.readlines()
    for line in all_lines:
        if line != '\n':
            print(line, end='')
