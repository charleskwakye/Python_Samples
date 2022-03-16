# r0879035
# Kwakye Charles Nana
# 1ACS
import random

list1 = []
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           list1.append(i)

x = random.randint(0,100)
print_factors(x)

counter = 1
for a in range(5):
    guessing_divider = input('Attempt' + str(counter) + ':')
    if guessing_divider not in list1:
        guessing_divider = input('Attempt' + str(counter) + ':')
        counter = counter + 1
    else:
        print('You only needed', counter, 'attempts')

print('The dividers for', x, 'are', list1)

