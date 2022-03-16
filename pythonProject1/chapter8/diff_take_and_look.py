print('Overview gifts')
print('Number of sponsors')
with open('Files chapter 8/sponsors.txt') as file:
    list = file.readlines()
    list.sort()
    print(list)
    i = 0
    total_number_forms = 0

    while i < len(list):
        record = list[i].rstrip().split('*')
        sponsor_id = record[0]
        amount = 0
        text_form =''
        print(str(sponsor_id) + "\t" + record[1] + ' ' + record[2], end='')
        while i < len(list) and record[0] == sponsor_id:
            amount = amount + int(record[3])
            i = i + 1
            if i < len(list):
                record = list[i].rstrip().split('*')
        if amount >= 40:
            total_number_forms += 1
            text_form = "**"
        print('\t' + str(amount) + '\t' + text_form)
    print('There are', total_number_forms, 'tax certificates to be sent.')






