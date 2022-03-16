with open('Files chapter 8/courses.csv') as inputfile:
    with open('Files chapter 8/student.csv', 'w') as outputfile:
        line = inputfile.readline()
        line = inputfile.readline().rstrip()
        info = line.split(';')

        while line:
            student_number = info[3]
            counter = 0
            whole_line = student_number + ';' + info[4]+ ';' + info[5]
            while line and info[3] == student_number:
                whole_line += ';' + info[1] + '(' + info[2] + ')'
                line = inputfile.readline().rstrip()
                info = line.rstrip().split(';')
            print(whole_line)
            outputfile.write(whole_line + '\n')




#########################
# print('#############################')
#
#
# with open('Files chapter 8/courses.csv') as inputfile:
#
#         line = inputfile.readline()
#
#
#         line = inputfile.readline().rstrip()
#         record=line.split(';')
#         while line:
#             studentid = record[3]
#             student_info = studentid+';'+record[4]+';'+record[5]
#             while line and record[3] == studentid:
#                 student_info +=';'+record[1]+'('+record[2]+')' #courses for each student
#                 line = inputfile.readline().rstrip()
#                 record = line.split(';')
#             print(student_info)



