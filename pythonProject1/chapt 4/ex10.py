result = ''
for i in range(1, 6):
    word = input('Enter a word' + str(i) + ':').capitalize()
    result = word + '' + result
print('The words in reverse order: ')
print(result)