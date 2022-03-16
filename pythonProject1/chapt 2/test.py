total = count = 0
# read the first number before the while
number = int(input('Enter a number, stop by entering -1: '))
while number != -1:
    count += 1   # count = count + 1
    total += number   # total = total + number
    # read the next number
    number = int(input('Enter a number, stop by entering -1: '))
print('Sum of the', count, 'numbers =', total)