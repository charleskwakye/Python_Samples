# Ex 6

text = input("Enter a text: ")
made_list = []
for letter in text :
    if letter != ' ' and letter not in made_list:
        made_list.append(letter)
        made_list.sort()
print(made_list)

counter = 0
for i in range(len(made_list)):
    print(made_list[counter], end = ' ')
    counter += 1

print(' ')
counter2 = 0
for i in range(len(made_list)):
    print(made_list[counter2], end = '   ')
    counter2 += 1