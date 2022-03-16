with open('Files chapter 8/classrooms.txt', encoding='utf-8') as file:
    line = file.readline().rstrip()
    info = line.split(';')


    while line:
        classroom = info[2]
        print('\n'+ classroom.rstrip() + ':')
        counter = 0
        while line and classroom == info[2]:
            print('\t' + info[1],info[0])
            line = file.readline().rstrip()
            info = line.split(';')
            counter += 1
        print('Number of students in classroom',classroom, '=', counter)
