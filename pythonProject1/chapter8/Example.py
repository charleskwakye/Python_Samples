print('Ex 1: Top cities in USA:')
with open('Files chapter 8/US cities.csv') as file:
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        state_indicative = record[1]
        #city_counter = 0
        max_population = int(record[2])
        max_city = int(record[0])
        print(state_indicative)
        while line and record[1] == state_indicative:
            #city_counter += 1
            #print('\t', city_counter, record[0])
            print('\t', record[0], '-', record[2])
            if int(record[2])>max_population:
                max_population = int(record[2])
                max_city = record[0]
            line = file.readline().rstrip()
            record = line.split(';')
    print('\tLargest population in',state_indicative,'- >', max_city,'-', max_population)
# group final instructions
# program final instructions
