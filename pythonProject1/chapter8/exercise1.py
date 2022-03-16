with open('Files chapter 8/classrooms.txt') as file:
    line = file.readline().rstrip()

    record = line.split(';')
    while line:
        room_indicative = record[2]
        number_per_room = 0
        print(room_indicative)
        while line and room_indicative == record[2]:

            number_per_room += 1
            print('\t', record[1], record[0])
            line = file.readline().rstrip()
            record = line.split(';')
        print('Number of students in classroom', room_indicative,'=', number_per_room)