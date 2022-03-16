letters = {'e': 1, 'h': 1, 'n': 1, 'o': 2, 't': 4}
my_choice = input('Letter? ')
print(letters.get(my_choice, 'This character does not occur'))
