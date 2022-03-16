with open('Files Chapter 7/kilometers.txt') as file:
    line = file.readline().rstrip()
    smallest = largest = int(line)
    while line:
        number = int(line)
        if number > largest:
            largest = number
        else:
            if number < smallest:
                smallest = number
        line = file.readline().rstrip()

print('The difference between the largest', '(',largest,'),', 'and smallest', '(',smallest,')', 'is', largest - smallest)