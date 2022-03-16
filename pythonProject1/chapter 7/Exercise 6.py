import random

number = random.randint(1,10)
print('Wish', number, '\n')
with open('Files Chapter 7/wish'+str(number)+'.txt') as file:
    print(file.read())
