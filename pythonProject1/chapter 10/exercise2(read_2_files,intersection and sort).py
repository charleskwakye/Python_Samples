set_1 = set()  # create empty set
set_2 = set()  # create empty set
with open('Files Chapter 10/first_names1ITF.txt', encoding='utf-8') as file1:
    line_1 = file1.readline().rstrip()  # read one line and strip

    while line_1:  # while there is a line
        set_1.add(line_1)  # add to set created earlier
        line_1 = file1.readline().rstrip()  # read another line again
with open('Files Chapter 10/first_names2ITF.txt', encoding='utf-8') as file_2:
    line_2 = file_2.readline().rstrip
    while line_2:
        set_2.add(line_2)
        line_2 = file_2.readline().rstrip()


print('In 1TF there are', len(set_1), 'different first names')
print('In 2TF there are', len(set_2), 'different first names')
set_both = set_1.intersection(set_2)  # name that appeared in both set
print('These are the', len(set_both), 'first names appear in 1ITF and 2ITF')
for element in sorted(set_both):
    print(element)


