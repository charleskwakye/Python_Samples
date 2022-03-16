appointments = []
appointments.append('This is the addition to the file created\n')
appointments.append('This is my second addition')

with open('Files Chapter 7/mine.txt', 'w', encoding='utf-8')as file:
    file.writelines(appointments)

