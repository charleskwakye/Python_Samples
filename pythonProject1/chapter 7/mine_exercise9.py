with open('Files Chapter 7/weather_2018 08.csv') as file:
    line = file.readline()
    while line:
        temp = line.split(';')

        largest = 0
        if temp[1].rstrip() > str(largest):
            largest = temp[1]
        line = file.readline()

print(largest)
