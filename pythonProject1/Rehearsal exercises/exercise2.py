def control(classroom):
    attendance_list = []
    with open('Files Chapter 12/classlist.csv', encoding='utf8') as file:

        line = file.readline()
        while line:
            record = line.rstrip().split(';')
            if record[3] == classroom:
                student = record[1] + ';' + record[2] + ';'
                in_or_no = input(record[2] + ' ' + record[1] + ':')
                if in_or_no.upper() == 'N':
                    attendance_line = student + 'NOT\n'
                    attendance_list.append(attendance_line)
                    line = file.readline()
                else:
                    attendance_line = student + 'OK\n'
                    attendance_list.append(attendance_line)
                    line = file.readline()
            else:
                line = file.readline()

    return attendance_list


user_input_class = input('In which class do you want to check: ')

new_list_attendance = control(user_input_class)

if len(new_list_attendance) == 0:
    print('This class does not exist')
else:
    with open('1 ACS 02.csv', 'w', encoding='utf8') as file:
        file.write('Attendance list' + user_input_class + '\n')
        for line in new_list_attendance:
            file.write(line)