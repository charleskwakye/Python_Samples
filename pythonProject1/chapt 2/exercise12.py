age = int(input('What is your age? '))

if 5< age <=7:
    feedb = 'Beavers'
elif 8< age <=10:
    feedb = 'Cubs'
elif 11< age <=13:
    feedb = 'Scouts'
elif 14< age <=18:
    feedb = 'Explorers'
elif age <= 5:
    feedb = 'too young!'
else:
    feedb = 'not eligible to be here'
print('Your age =',age,'\n You are',feedb)
