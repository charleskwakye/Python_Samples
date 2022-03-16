print('A boolean program')
is_morning = True
is_mother = True
is_asleep = False

if is_asleep:
    reaction = 'I am not answering the call'
else:
    if is_morning and not is_mother:
        reaction = 'I am not answering the call'
    else:
        reaction = 'I am answering the call'
print(reaction)
