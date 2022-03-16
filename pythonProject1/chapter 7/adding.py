with open('Files Chapter 7/mine.txt', 'a', encoding='utf-8') as file:
    appointments = []
    appointments.append('\nThis is me adding to the file\n')
    appointments.append('Second additions to the file with thing in it')
    file.writelines(appointments)