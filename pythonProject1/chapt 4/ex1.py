colour = input('What is your favorite colour: ')
print(colour[0]+colour[2])
print('This colour consist of', len(colour), 'letters')
print()
for item in colour:
    print(item, '=', ord(item))
print()
i = 0
while i < len(colour):
    if i % 2 == 0:
        print('#'+colour[i]+'#')
    else:
        print('**'+colour[i]+'**')
    i += 1
