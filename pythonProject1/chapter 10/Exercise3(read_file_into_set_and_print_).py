classes = set()
with open('Files Chapter 10/local_booking.txt') as file:
    line = file.readline().rstrip()
    record = line.split(';')[3]

    while line:
        record = line.split(';')[3]
        if record not in classes:
            classes.add(record)
        line = file.readline().rstrip()



for element in classes:
    print(element)