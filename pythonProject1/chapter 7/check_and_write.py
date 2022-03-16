from os.path import exists

if exists('Files Chapter 7/mine_3.txt'):
    with open('Files Chapter 7/mine_3.txt', encoding='utf-8') as file:
        line = file.read()
        print(line)
else:
    with open('Files Chapter 7/mine_3.txt', 'w', encoding='utf-8') as file:
        appointments = []
        appointments = ('This is it')
        file.writelines(appointments)
        print('created new file')