fnum = int(input('Enter the first number: '))
if fnum < 0:
    fnum *= -1
snum = int(input('Enter the second number: '))
if snum < 0:
    snum *= -1

if fnum == snum:
    answer = 0
else:
    if fnum % 5 == 0 and snum % 5 == 0:
        if fnum < snum:
            answer = fnum
        else:
            answer = snum
    else:
        if fnum > snum:
            answer = fnum
        else:
            answer = snum
print('The answer for the numbers', fnum, 'and', snum, '=', answer)
