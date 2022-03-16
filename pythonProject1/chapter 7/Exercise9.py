with open('Files Chapter 7/weather_2018 08.csv', encoding='utf-8') as file:
    lines = file.readlines()
    temperature = 0
    for line in range(1,len(lines)):
        whole_line = lines[line].split(';')
        temp = whole_line[1]
        if temp > str(temperature):
            temperature = temp



print('The highest temperature in this record is', temperature + '°C')
