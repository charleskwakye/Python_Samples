text = input('Enter a text consisting of letter and numbers: ')
digits = set()
letters = set()

for element in text:
    if element.isdigit():
        digits.add(element)
    else:
        letters.add(element)
print('The numbers: ')
for digit in digits:
    print(digit)
print('The letters')
for letter in letters:
    print(letter)