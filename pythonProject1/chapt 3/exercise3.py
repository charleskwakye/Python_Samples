myage = int(input('How old are you: '))
fathers_age = int(input('How old is your father: '))
counter =0
while myage * 2 < fathers_age:
   myage += 1
   fathers_age += 1
   counter += 1

if counter == 0:
    print('The situation is no longer possible for these ages')
else:
    print('Within',counter,' years, your father will have twice your age')
    print('Your father will be',fathers_age,'and you will be',myage)