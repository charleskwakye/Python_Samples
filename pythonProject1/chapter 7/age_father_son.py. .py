age_son = int(input('How old are you: '))
age_father = int(input('How old is your father: '))
counter = 0

while age_son * 2 < age_father:
    age_son += 1
    age_father += 1
    counter += 1

if counter == 0:
    print('The situation is no longer possible for your ages')
else:
    print('Within', counter, 'years your father will have twice your age')
    print('Your father will be', age_father, 'and you will be', age_son)