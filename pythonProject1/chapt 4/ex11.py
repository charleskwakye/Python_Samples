text = input("Enter a text: ")
is_followed = True
for i in range(len(text)):
    if text[i] == 'x':
        if text[i:].find('y') == -1:
            is_followed = False
if is_followed:
    print('In this text every x is followed by a y.')
else:
    print('In this text not every x is followed by a y.')
    