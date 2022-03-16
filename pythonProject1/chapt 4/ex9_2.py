bread = 'sandwich'
word = input('What do you eat for lunch: ')
times = word.count(bread)
result = 'You have XXX between your sandwich.'
if times == 2:
    pos = word.find(bread)
    new_word = word[pos + len(bread):]
    pos = new_word.find(bread)
    content = new_word[:pos]
    result = result.replace('XXX',content)
else:
    result = ''
print(result)
