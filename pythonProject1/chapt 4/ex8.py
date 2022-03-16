word = input('Enter a word: ')
if word.find('in') in (0, 1):  # first or second
    print("'in' appears in the first or second place")
elif word.find('in') == -1:  # not found
    print("this word does not contain 'in'")
else:
    print("'in' appears in the word but not in the front")
