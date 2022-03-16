boys = []
girls = []
with open('Files Chapter 7/contacts.csv') as file:
    line = file.readline()
    while line:
        record = line.split(';')

        if record[3].rstrip() == "M":
            boys.append(record[1]+''+record[0])
        else:
            girls.append(record[1]+''+record[0])
        line = file.readline()

boys.sort()

print(len(girls),'girls: ')
for item in girls:
    print('\t', item)
print(len(girls), 'boys: ')
for item in boys:
    print('\t', item)
