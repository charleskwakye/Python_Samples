print('Average temperatures:')
with open('Files chapter 8/weather_2018 10.csv') as file:
    line = file.readline()
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        date = record[0].split(' ')[0]
        counter = 0
        temp = 0
        while line and record[0].split(' ')[0] == date:
            counter += 1
            temp += float(record[1])
            line = file.readline().rstrip()
            record = line.split(';')
        print(date + '\t number of measurements = ', str(counter) + '\t average =', '{:.4}'.format(temp/counter))
print('>'*60)