import random

#secretnum = 56
secretnum = random.randint(1,15)
guess = int(input('Enter a positive number: '))
count =1
while guess != secretnum:
    if guess < secretnum:
        feedback = 'Lower!'
        count+=1

    elif guess > secretnum:
        feedback = 'Higher!'
        count+=1

    print(feedback)
    guess = int(input('Enter a positive number: '))
print('You have guessed the number',guess,'in',count,'turns')