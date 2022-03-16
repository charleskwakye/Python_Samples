word = input('Enter a word: ')
characters = {}
# go through letters in word
for letter in word:
    # check if letter is present in dictionary
    if letter in characters:
        characters[letter] += 1
        # increase value via key
    else:
        characters[letter] = 1
        # create new key/value pair
# print key/value pairs
for character in characters:
    print(character, characters[character])