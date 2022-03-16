numzero = numsix =0
num = int(input('enter a number: '))
while num > 0:
    remainder = num%10
    if remainder ==0:
        numzero+=1
    elif remainder ==6:
        numsix+=1
    num=num//10
print('The number consist of',numzero,'zeros and',numsix,'sixes')

