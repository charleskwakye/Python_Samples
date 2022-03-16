with open('Files Chapter 7/books.txt') as file:
    lines = file.readlines()
    counter = 0
    for i in range(0,len(lines),2):
        counter +=1
        print(counter,lines[i].rstrip(), '->', lines[i+1].rstrip())