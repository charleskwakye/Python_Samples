text = input('Enter a text: ')
length = largest = 1
for i in range(len(text)-1):  # if you dont include a -1 you will get an infinite loop
    if text[i] == text[i+1]:
        length += 1
    else:
        length = 1
    if length > largest:
        largest = length
print('The length of the largest block in this text is', largest)
