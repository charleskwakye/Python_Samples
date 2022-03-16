# r0879035
# Kwakye Charles Nana
# 1ACS


#character = input('Enter a character until which you would like to show you word: ')



word = input('Enter a word: ')
while word != -1:
    character = input('Enter a character until which you would like to show you character: ')
    x = word.find(character)
    number_of_letters = len(word) - x
    print('Result:', word[0:x])
    print(number_of_letters, 'characters have been removed')
    word = input('Enter a word: ')