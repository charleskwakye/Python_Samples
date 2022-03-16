import random

number = random.randint(1,10)
with open('table' + str(number)+'.txt','w') as output_file:
    for i in range(1, 11):
        output_file.write(str(i)+'x'+str(number)+'='+str(i*number)+'\n')
