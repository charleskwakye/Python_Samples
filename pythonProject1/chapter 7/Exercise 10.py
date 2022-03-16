with open('age_father_son.py. .py', encoding='utf-8') as file:
    lines = file.readlines()
    code_list = []
    for line in lines:
        code_list.append(line.rstrip())

with open('code.txt', 'w', encoding='utf-8') as file:
    counter = 0
    for items in code_list:
        counter += 1
        file.write('{:4}'.format(counter) + ' ' + items + '\n')