#file = open('Files Chapter 7/students.txt')
#print(file.read())
#file.close()

#with open('Files Chapter 7/students.txt') as file:
    #print(file.read())

# readline() reading line after line
#with open('Files Chapter 7/students.txt') as file:
#    line = file.readline()  # step 1 read the line
#    while line:  # step 2 checking condition
#        if line != '\n':  # step 3 doing something
#            print(line.rstrip())
#        line = file.readline()  # step 4 reading next line

#with open('Files Chapter 7/students.txt') as file:
#    line = file.readline()  # step 1 read the line
#    while line:  # step 2 checking condition
#        if line != '\n':  # step 3 doing something
#            record = line.split()
#            print(record[0], record[1])
#        line = file.readline()  # step 4 reading next line


with open('Files Chapter 7/students.txt') as file:
    lines = file.readline
    print(lines)