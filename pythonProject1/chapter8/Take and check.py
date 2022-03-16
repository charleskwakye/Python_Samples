with open('Files chapter 8/classrooms.txt', encoding='utf-8') as file:
    line = file.readline().rstrip()
    info = line.split(';')
    record = []


    while line:
        classroom = info[2]
        counter = 0
        while line and info[2] == classroom:
            counter += 1
            line = file.readline().rstrip()
            info = line.split(';')
        record.append([classroom,counter])
print(record)
