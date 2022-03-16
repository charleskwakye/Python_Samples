with open('Files chapter 8/sponsors.txt') as file:
    list = file.readlines()
    list.sort()
    i = 0
while i < len(list):
    record = list[i].rstrip().split('*')
    sponsorid = record[0]
    total_per_sponsor = 0
    while i <len(list) and record[0] == sponsorid:
        total_per_sponsor+= int(record[3])
        i +=1
        if i < len(list):
            record = list[i].rstrip().split('*')
    print(total_per_sponsor)

