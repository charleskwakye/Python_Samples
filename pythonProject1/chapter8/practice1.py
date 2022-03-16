with open('Files chapter 8/sponsors.txt') as file:
    lines = file.readlines()
    lines.sort()
    i = 0

while i < len(lines):
    record = lines[i].rstrip().split('*')
    sponsor_id = record[0]
    amount = 0
    while i < len(lines) and record[0] == sponsor_id:
        amount += int(record[3])
        i = i + 1
        if i < len(lines):
            record = lines[i].rstrip().split('*')
    print(amount)