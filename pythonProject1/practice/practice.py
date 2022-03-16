with open("schedule.txt") as file:
    line = file.readline()
    while line:
        if line != '\n':
            record = (line.split(';'))
            print(record[1])
        line = file.readline()
