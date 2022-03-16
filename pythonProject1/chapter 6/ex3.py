# def print_square(number, character):
#     for i in range(number):
#         print(character * number)
#
#
# number = int(input("Enter a number: "))
# character = input("Enter a character: ")
#
# print_square(number, character)


def print_square(number,character):
    for i in range(number):
        print(character*number)

char = input('Which character do you want to use (enter to stop): ')

while char != '':
    no = int(input('Number of character per line: '))
    print_square(no, char)
    char = input('Which character do you want to use (enter to stop): ')
